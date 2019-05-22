from django.core.management.base import BaseCommand

from googleapiclient.discovery import build
from dotenv import load_dotenv


from .vectorizer import vect

import os
import pickle
import numpy as np
import pandas as pd
import json

from songs.models import NewVideo, NewVideoDescription

# pickeled ML algorithms
classifier = pickle.load(open(
    os.path.join('pkl_objects',
        'classifier.pkl'), 'rb'))

def classify(description):
    label = {0: 'ANGRY', 1: 'CHILL', 2: 'CONFIDENT-SASSY', 3: 'HAPPY', 4: 'IN-LOVE', 5: 'SAD'}
    X = vect.transform([description])
    pred = classifier.predict(X)[0]
    return label[pred]

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
        part='id,snippet',
        #maxResults=20,
        id=video_id,
        #q='instrumental no copyright music',
        #relevanceLanguage='en',
        #type='video',
        #videoDuration='medium',
        #videoLicense='creativeCommon',
        #videoSyndicated='true',
        #fields=items(contentDetails/hasCustomThumbnail,snippet,statistics,status,suggestions,topicDetails)
    ).execute()

    videos = []
    result_count = 0

    #new_videos = NewVideo.objects.all()

    for search_result in request['items']:
        video_title             = search_result['snippet']['title']
        video_title             = html_reverse_escape(video_title)
        video_id                = video_id
        video_description       = search_result['snippet']['description']
        predicted_moods         = classify(video_description)
        #video_id                = search_result['id']['videoId']
        #video_view_count        = search_result['statistics']['viewCount']
        #video_like_count        = search_result['statistics']['likeCount']
        #video_favorite_count    = search_result['statistics']['favoriteCount']
        #video_comment_count     = search_result['statistics']['commentCount']
      
        try:
            new_videos_description = NewVideoDescription(
                video_id=video_id,
                video_title=video_title,
                video_description=video_description,
                predicted_moods=predicted_moods
            )
            """
            new_videos = (NewVideo.query.get(video_id) or
                NewVideo(video_id=video_id, video_title=video_title))
            """
            new_videos_description.save()
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


