from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Movie(models.Model):
	title = models.TextField()
	slug = models.SlugField()
	year = models.IntegerField()
	director = models.TextField()