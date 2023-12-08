from django.urls import path,include
from . import views

urlpatterns=[
    path("movies",views.MovieListView.as_view(),name="movies-list"),
    path("movie/<int:pk>/",views.MovieView.as_view(),name="movie")
]