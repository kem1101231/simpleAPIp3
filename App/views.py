from types import MethodDescriptorType, ModuleType
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Movies


def movies(request):
    movies = Movies.objects.all()
    context = {
        'movies':list(movies.values()),
    }

    try:
        return JsonResponse(context)
    except:
        return HttpResponse("No movies to display")

def addMovie(request):

    if request.method == 'POST':
        title = request.get['title']
        year_of_release = request.get['year_of_release']

        movie = Movies(title=title, year_of_release=year_of_release)
        movie.save()

    return HttpResponse("Done adding")

def getMovieDetails(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    movie_detail = {
        'title':movie.title,
        'year_of_realease':movie.year_of_release,
    }

    context = {
        'movie':movie_detail,
    }

    return JsonResponse(context)