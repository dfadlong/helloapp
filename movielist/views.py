from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from movielist.models import Movie

from django.template import Context, loader

def show_movie(request):
	movie_list = Movie.objects.all()
	template = loader.get_template(
		'movielist/movie_detail.html')
	# Only take the first movie.
	context = Context({'m': movie_list[0]})
	output = template.render(context)
	return HttpResponse(output)
