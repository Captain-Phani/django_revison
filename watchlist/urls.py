from django.urls import path
from . import views

urlpatterns=[
    path('watchlistmovies',views.WatchListView.as_view(),name='watchlist-movies'),
    path('watchlistmovie/<int:pk>/',views.WatchMovieView.as_view(),name='watchlist-movie'),
    path('streamingPlatforms/',views.StreamingPlatformListViews.as_view(),name='StreamList'),
    path('streamingPlatform/<int:pk>/',views.StreamPlarformView.as_view(),name='streaming-platform')
]