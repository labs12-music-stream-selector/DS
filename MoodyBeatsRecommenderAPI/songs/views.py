from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from braces.views import PrefetchRelatedMixin

# Create your views here.
from django.views.generic import (
	ListView,
	DetailView,
)

from .models import Song, NewVideo


class SongListView(ListView):
	#model = Song
	template_name = 'songs/list_view.html'
	paginate_by = 7

	def get_queryset(self, *args, **kwargs):
		qs = Song.objects.all().order_by('id')
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(songs__icontains=query)|
				Q(tags__name__icontains=query)|
				Q(mood__icontains=query)|
				Q(recommendation_one__icontains=query)|
				Q(recommendation_two__icontains=query)|
				Q(recommendation_three__icontains=query)|
				Q(recommendation_four__icontains=query)|
				Q(recommendation_five__icontains=query)
			)
		return qs
		
	
class SongDetailView(DetailView):
    queryset = Song.objects.all()



class NewVideoListView(ListView):
    template_name = 'songs/new_video_list_view.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = NewVideo.objects.all().order_by('video_id')
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(video_title__icontains=query)|
                Q(moods__icontains=query)|
                # you need the __topics from NewVideo tags because it's a reverse relation
                Q(new_video_tags__topics__icontains=query)
            )
        return qs









"""
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

import pandas as pd
import json

load_dotenv()

def html_reverse_escape(string):
    '''Reverse escapes HTML code in string into ASCII text.'''
    # see Ned Batchelder post https://stackoverflow.com/questions/2077283/escape-special-html-characters-in-python
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))



def search_api():
    '''Searches YouTube Data API v3 for videos based on project-specified parameters; returns list of videos.'''
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part='id,snippet',
        maxResults=50,
        q='instrumental',
        relevanceLanguage='en',
        type='video',
        videoDuration='medium',
        videoLicense='creativeCommon',
    ).execute()

    videos = []
    result_count = 0

    for search_result in request['items']:
        video_title = search_result['snippet']['title']
        video_title = html_reverse_escape(video_title)
        video_id = search_result['id']['videoId']


    #return video_title, video_id

    
        # videos.append((video_title, video_id))
    
    
    videos = pd.Series(videos).to_json()
    parsed = json.loads(videos)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    print(videos)
    
    return videos
	"""








