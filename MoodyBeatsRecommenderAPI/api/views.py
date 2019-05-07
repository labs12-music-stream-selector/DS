from django.shortcuts import render

from rest_framework import generics
from songs.models import Song
from .serializers import SongSerializer

class SongListAPIView(generics.ListCreateAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	#lookup_field = 'slug'

