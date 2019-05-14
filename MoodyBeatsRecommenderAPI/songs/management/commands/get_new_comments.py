from django.core.management.base import BaseCommand

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

import pandas as pd
import json


from songs.models import NewVideo, NewComment

load_dotenv()

#video_id = 'stTd98I8F4Y'

def html_reverse_escape(string):
    '''Reverse escapes HTML code in string into ASCII text.'''
    # see Ned Batchelder post https://stackoverflow.com/questions/2077283/escape-special-html-characters-in-python
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))


def search_comments(video_id):
    '''Searches YouTube Data API v3 for videos based on project-specified parameters; returns list of videos.'''
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    #threads = []
    results = youtube.commentThreads().list(
    	part="snippet",
    	videoId=video_id,
    	textFormat="plainText",
    ).execute()

    comments = []
    for item in results["items"]:
        # threads.append(item)
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        video_id = video_id
        # comment = item["snippet"]["textDisplay"]
        comments.append(comment)

    try:
        new_comments = NewComment(video_id=video_id, comments=comments)
        new_comments.save()
    except:
        pass

        # text = html_reverse_escape(text)
    	#comments.append(text)


    # comments = pd.Series(comments).to_json()
    # parsed = json.loads(comments)

    # print(comments)
    # return comments
    # return text

    #threads = pd.Series(threads).to_json()
    #parsed = json.loads(threads)
    #print(json.dumps(parsed, indent=4, sort_keys=True))
    #print(threads)

    #return threads

#if __name__ == '__main__':
    #search_comments()

def get_all_comments():
    for video in NewVideo.objects.all():
        results = search_comments(video_id=video.video_id)
    #print(results)
    return results

# def get_all_comments():
#     video_id_list = [video.video_id for video in NewVideo.objects.all()]
#     for i in video_id_list:
#         results = search_comments(i)
#         #print(results)
#         return results

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Pulling data from YouTube API")
        get_all_comments()



