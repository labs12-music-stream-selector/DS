from django.conf.urls import url, include

from .views import (
	SongListAPIView,
	SongDetailAPIView,
	NewVideoAPIView,
	NewVideoDetailAPIView,
	NewCommentAPIView,
	NewVideoStatsAPIView,
	NewVideoStatsDetailAPIView,
	NewVideoCorrectMoodAPIView,
	NewVideoCorrectMoodDetailAPIView,
)

urlpatterns = [
	url(r'^$', SongListAPIView.as_view(), name='api'),
	url(r'^new-videos/$', NewVideoAPIView.as_view()),
	url(r'^new-videos/(?P<video_id>[\w-]+)/$', NewVideoDetailAPIView.as_view()),
	url(r'^new-comments/$', NewCommentAPIView.as_view()),

	url(r'^new-videos-stats/$', NewVideoStatsAPIView.as_view()),
	url(r'^new-videos-stats/(?P<video_id>[\w-]+)/$', NewVideoStatsDetailAPIView.as_view()),

	url(r'^new-videos-moods/$', NewVideoCorrectMoodAPIView.as_view()),
	url(r'^new-videos-moods/(?P<video_id>[\w-]+)/$', NewVideoCorrectMoodDetailAPIView.as_view()),
	#url(r'^(?P<slug>)[\w-]+/$', SongDetailAPIView.as_view()),
	#url(r'^(?P<slug>[\w-]+)/$', SongDetailAPIView.as_view()),
	url(r'(?P<pk>\d+)/$', SongDetailAPIView.as_view()),
]


