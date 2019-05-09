from django.conf.urls import url, include

from .views import SongListView, SongDetailView

urlpatterns = [
	url(r'^$', SongListView.as_view(), name='song'),
	url(r'^tag/(?P<tag_slug>[-\w]+)/$', SongListView.as_view(), name='song_by_tag'),
	url(r'^(?P<slug>[\w-]+)/$', SongDetailView.as_view(), name='detail'),
	#url(r'(?P<pk>\d+)/$', SongDetailView.as_view(), name='detail'),
]

