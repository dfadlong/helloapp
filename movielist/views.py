from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from movielist.models import Movie

from django.template import Context, loader

def show_movie(request):
	year = request.GET.get('year', '')
	page = int(request.GET.get('page', '0'))

	if year:
		movie_list = Movie.objects.filter(year=year)
	else:
		movie_list = Movie.objects.all()
	num = len(movie_list)
	template = loader.get_template(
		'movielist/movie_detail.html')
	# Only take the first movie.
	context = {
		'movies': movie_list[page * 10: page * 10 + 10],
		'num': num,
		'year': year,
		'next_page': page + 1,
	}
	output = template.render(context)
	return HttpResponse(output)
