from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from movielist.models import Movie

def show_movie(request):
	m = Movie.objects.all()

	text = ''
	for k in m:
		text += '<p>' + k.title + '</p>'

	return HttpResponse(text)
