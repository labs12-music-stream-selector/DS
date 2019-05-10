from django.shortcuts import render

from rest_framework import generics
from songs.models import (
	Song,
	Tag,
	NewVideo
)

from .serializers import SongSerializer, NewVideoSerializer

class SongListAPIView(generics.ListCreateAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	#lookup_field = 'slug'

class NewVideoAPIView(generics.ListCreateAPIView):
	queryset = NewVideo.objects.all()
	serializer_class = NewVideoSerializer




