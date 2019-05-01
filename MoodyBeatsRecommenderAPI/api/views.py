from django.shortcuts import render

from rest_framework import generics
from songs.models import Song
from .serializers import SongSerializer

class SongListAPIView(generics.ListAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailAPIView(generics.RetrieveAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	#lookup_field = 'slug'

