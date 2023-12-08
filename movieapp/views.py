from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import MovieSerializer
from .models import Movies
from rest_framework import status

# Create your views here.

# @api_view(['GET','POST'])  #------------>It represents what kind of request we are requesting to browser by default it will consider "get" method
# def get_movies(request):
#     if request.method=='GET':
#
#         movies=Movies.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         print(serializer)
#         return Response(serializer.data)
#
#     if request.method=="POST":
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
#
#
class MovieNotFoundException(Exception):
    def __init__(self,pk):
        """
        Custom exception is created by inheriting in built exception class.
        """
        self.pk=pk
        super().__init__(f'Movie with {self.pk} does not exist')


def get_movie_or_raise_404(pk):
    """
        This method is responsible for raising error if object with id is not found
    """
    try:
        movie=get_object_or_404(Movies,pk=pk)
        return movie
    except Http404:
        raise MovieNotFoundException(pk)


        # return Response({'detail': f'Movie with id {pk} does not exist'},status=status.HTTP_404_NOT_FOUND)
#
# @api_view(['GET','PUT','DELETE'])   #------------>It represents what kind of request we are requesting to browser
# def get_movie(request,pk):
#     try:
#         movie = get_movie_or_raise_404(pk=pk)
#         if request.method=='GET':
#             serializers=MovieSerializer(movie)
#             print(serializers.data)
#             return Response(serializers.data)
#
#         if request.method=='PUT':
#             movie=Movies.objects.get(pk=pk)
#             serializer=MovieSerializer(movie,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#
#         if request.method=='DELETE':
#             movie=Movies.objects.get(pk=pk)
#             movie.delete()
#             return Response({"detail":"Succesfully Deleted"},status=status.HTTP_204_NO_CONTENT)
#
#     except MovieNotFoundException as e:
#         return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)


class MovieListView(APIView):
    def get(self,request):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    def get(self,request,pk):
        try:
            movie=get_movie_or_raise_404(pk)
            serializer=MovieSerializer(movie)
            return Response(serializer.data)

        except MovieNotFoundException as e:
            return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk):
        try:
            movie = get_movie_or_raise_404(pk=pk)
            serializer = MovieSerializer(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except MovieNotFoundException as e:
            return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        try:
            movie=get_movie_or_raise_404(pk=pk)
            movie.delete()
            return Response("Successfully Deleted")
        except MovieNotFoundException as e:
            return Response({'detail':str(e)},status=status.HTTP_404_NOT_FOUND)









