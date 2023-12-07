from django.urls import path,include
from . import views

urlpatterns=[
    path("movies",views.get_movies,name="movies-list"),
    path("movie/<int:pk>/",views.get_movie,name="movie")
]