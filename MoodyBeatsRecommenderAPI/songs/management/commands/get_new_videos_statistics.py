from django.core.management.base import BaseCommand

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

import pandas as pd
import json

from songs.models import NewVideo, NewVideoStats

load_dotenv()

def html_reverse_escape(string):
    '''Reverse escapes HTML code in string into ASCII text.'''
    # see Ned Batchelder post https://stackoverflow.com/questions/2077283/escape-special-html-characters-in-python
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))

#video_id = 'YgFoI_tykWc'

def search_statistics(video_id):
    '''Searches YouTube Data API v3 for videos based on project-specified parameters; returns list of videos.'''
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    request = youtube.videos().list(
        part='snippet,statistics',
        maxResults=20,
        id=video_id,
        #q='instrumental no copyright music',
        #relevanceLanguage='en',
        #type='video',
        #videoDuration='medium',
        #videoLicense='creativeCommon',
        #videoSyndicated='true',
    ).execute()

    videos = []
    result_count = 0

    #new_videos = NewVideo.objects.all()

    for search_result in request['items']:
        video_title             = search_result['snippet']['title']
        video_title             = html_reverse_escape(video_title)
        video_id                = video_id
        #video_id                = search_result['id']['videoId']
        video_view_count        = search_result['statistics']['viewCount']
        video_like_count        = search_result['statistics']['likeCount']
        video_favorite_count    = search_result['statistics']['favoriteCount']
        #video_comment_count     = search_result['statistics']['commentCount']
      
        try:
            new_videos_stats = NewVideoStats(
                video_id=video_id,
                #video_title=video_title,
                video_view_count=video_view_count,
                video_like_count=video_like_count,
                video_favorite_count=video_favorite_count,
                #video_comment_count=video_comment_count,
                new_video_id=video_id
            )
            """
            new_videos = (NewVideo.query.get(video_id) or
                NewVideo(video_id=video_id, video_title=video_title))
            """
            new_videos_stats.save()
        except Exception as e:
            return e

        """
        if search_result['id']['videoId'] not in [i.video_id for i in new_videos]:
            new_videos = NewVideo.objects.create(video_id=search_result['id']['videoId'],
                video_title=html_reverse_escape(search_result['snippet']['title']))
            new_videos.save()
        """
  
def get_all_statistics():
    for video in NewVideo.objects.all():
        results = search_statistics(video_id=video.video_id)
    #print(results)
    return results


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Pulling data from YouTube API and saving")
        #search_statistics()
        get_all_statistics()
        
