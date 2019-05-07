from django.conf.urls import url, include

from .views import SongListAPIView, SongDetailAPIView

urlpatterns = [
	url(r'^$', SongListAPIView.as_view(), name='api'),
	#url(r'^(?P<slug>)[\w-]+/$', SongDetailAPIView.as_view()),
	#url(r'^(?P<slug>[\w-]+)/$', SongDetailAPIView.as_view()),
	url(r'(?P<pk>\d+)/$', SongDetailAPIView.as_view()),
]


