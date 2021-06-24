from types import MethodDescriptorType, ModuleType
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import ast

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

@csrf_exempt
def addMovie(request):

    if request.method == 'POST':
        print("POST bay")

        request_body = request.body
        request_dict = request_body.decode("UTF-8")
        result = ast.literal_eval(request_dict)
        print(result)
        # print(request.POST)
        # print(request.body)
        # print(type(request.body))
        # print(request.body[0])
        title = result['title']
        year_of_release = result['year_of_release']

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

def funtest(request):
    print(request.GET.get('data1'))
    print(request.GET)
    return HttpResponse("FFFFFF")