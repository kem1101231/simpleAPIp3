from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name="Movies"), 
    path('<int:movie_id>/details/', views.getMovieDetails, name="Movie Details"), 
    path('test/', views.funtest, name="Func"), 
    path('add_movie/', views.addMovie, name="Add Movie"),
]
