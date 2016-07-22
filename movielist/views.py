from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404

from movielist.models import Movie

from django.template import Context, loader

def show_movie(request):
	director = request.GET.get('director', '')
	page = int(request.GET.get('page', '0'))

	if director:
		movie_list = Movie.objects.filter(director=director)
	else:
		movie_list = Movie.objects.all()
	num = len(movie_list)
	template = loader.get_template(
		'movielist/movie_detail.html')

	if page < len(movie_list) / 10:
		next_page = page + 1
	else:
		next_page = None
		
	context = {
		'movies': movie_list[page * 10: page * 10 + 10],
		'num': num,
		'director': director,
		'next_page': next_page,
	}
	output = template.render(context)
	return HttpResponse(output)


def show_single_movie(request, slug):
	try:
		movie = Movie.objects.get(slug=slug)
	except Movie.DoesNotExist:
		return HttpResponse('Not found')
	template = loader.get_template(
		'movielist/movie_detail.html')
	context = Context({'movies': [movie]})
	output = template.render(context)
	return HttpResponse(output)

