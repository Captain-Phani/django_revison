from django.shortcuts import render,get_object_or_404
from watchlist.models import Watchlist,StreamPlatform
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import WatchlistSerializer,StreamPlatformSerializers


# class StreamingPlatformNotFoundError(Exception):
#     """
#     customizing exception
#     """
#     def __init__(self,pk):
#         self.pk=pk
#         super().__init__(f'streaming platform with id:{self.pk} does not exist')


class MovieNotFoundError(Exception):
    """
    customizing exception
    """
    def __init__(self,pk):
        self.pk=pk
        super().__init__(f'Movie with id:{self.pk} does not exist')

def get_movie_or_raise_error(obj,pk):
    """
    passing pk as param if param exist in Watchlist it will return obj or it raises MovieNotFoundError

    :param pk:
    :return:
    """
    try:
        movie=get_object_or_404(obj,pk=pk)
        return movie

    except:
        raise MovieNotFoundError(pk)


# Create your views here.
#WatchlistViews
class WatchListView(APIView):

    def get(self,request):
        movies=Watchlist.objects.all()
        serializers=WatchlistSerializer(movies,many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers=WatchlistSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)




class WatchMovieView(APIView):
    """
    class to retrieve a single object from queryset
    """
    def get(self,request,pk):
        try:
            movie=get_movie_or_raise_error(Watchlist,pk)
            print(movie)
            serializers=WatchlistSerializer(movie)
            return Response(serializers.data)
        except MovieNotFoundError as e:
            return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        try:
            movie=get_movie_or_raise_error(Watchlist,pk)
            serializers=WatchlistSerializer(movie,data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return serializers.errors
        except MovieNotFoundError as e:
            return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        try:
            movie=get_movie_or_raise_error(Watchlist,pk)
            movie.delete()
            return Response('Successfully Deleted')
        except MovieNotFoundError as e:
            return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)


#StreamList
class StreamingPlatformListViews(APIView):
    def get(self,request):
        platforms=StreamPlatform.objects.all()
        serializers=StreamPlatformSerializers(platforms,many=True,context={'request': request})
        return Response(serializers.data)

    def post(self,request):
        serializers=StreamPlatformSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

#Retrieving Stream platform by id
class StreamPlarformView(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)

            serializers=StreamPlatformSerializers(platform)
            return Response(serializers.data)
        except StreamPlatform.DoesNotExist:

            return Response({'detail': f'stream with id: {pk} Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
            serializers=StreamPlatformSerializers(platform,data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        except StreamPlatform.DoesNotExist:

            return Response({'detail': f'stream with id: {pk} Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
            platform.delete()
            return Response("Platform Successfully Deleted")
        except StreamPlatform.DoesNotExist:

            return Response({'detail':f'stream with id: {pk} Not found'},status=status.HTTP_404_NOT_FOUND)






