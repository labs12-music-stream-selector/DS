from django.shortcuts import render

from rest_framework import generics, viewsets, permissions

from songs.models import (
	Song,
	Tag,
	NewVideo,
	NewComment,
	NewVideoTag,
	NewVideoStats,
	NewVideoCorrectMood,
)

from .serializers import (
	SongSerializer,
	NewVideoSerializer,
	NewVideoDetailSerializer,
	NewCommentSerializer,
	NewVideoStatsSerializer,
	#NewVideoStatsDetailSerializer,
	NewVideoCorrectMoodSerializer,
)

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

class NewVideoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = NewVideo.objects.all()
	serializer_class = NewVideoDetailSerializer
	lookup_field = 'video_id'

class NewCommentAPIView(generics.ListCreateAPIView):
	queryset = NewComment.objects.all()
	serializer_class = NewCommentSerializer

class NewVideoStatsAPIView(generics.ListAPIView):
	queryset = NewVideoStats.objects.all()
	serializer_class = NewVideoStatsSerializer

class NewVideoStatsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = NewVideoStats.objects.all()
	serializer_class = NewVideoStatsSerializer
	lookup_field = 'video_id'

class NewVideoCorrectMoodAPIView(generics.ListCreateAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = NewVideoCorrectMoodSerializer
	queryset = NewVideoCorrectMood.objects.all()

class NewVideoCorrectMoodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = NewVideoCorrectMoodSerializer
	queryset = NewVideoCorrectMood.objects.all()
	lookup_field = 'video_id'



"""
class NewVideoStatsDetailAPIView(generics.RetrieveAPIView):
	#queryset = NewVideoStats.objects.all()
	serializer_class = NewVideoStatsDetailSerializer
	lookup_field = 'video_id'
	
	def get_queryset(self):
		queryset = NewVideoStats.objects.all()
		new_video = self.request.query_params.get('new_video', None)
		if new_video is not None:
			queryset = queryset.filter(new_video=new_video)
		return queryset
"""



