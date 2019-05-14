from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# import pandas as pd
import json


#from songs.models import NewVideo

load_dotenv()

# this is a video id for one comment threads
video_id = 'stTd98I8F4Y'

# this is a list of all the video_id in my django database which you can iterate over, but i dont' know how
video_id_list = ['stTd98I8F4Y', '-QQUaWtMW3w', 'L0aG7qRmZd8', 'rA2eMqLk89Q', '5vSJTGpG5YM',
 'gnxnQZaVkGM', 'FWuV5QDm2ZM', '8g9TgP0uLFI', 'b4T5TuaUab8', 'raihkbCDBw4',
  '28vPJrMDYmc', 'Vpy-ivqbffw', 'Bbc7znh6i6g', '2raUmsKIG6U', 'NuCsDnTkEYU',
   'YDcvOjj0xBg', 'Jjs9C8Gb0Xw', 'nISU9BUm9E0', 'WJjxHNnebtM', '3XAkH0w3QLc']


def html_reverse_escape(string):
    '''Utility to reverse escape HTML code in string into ASCII text.'''
    # see Ned Batchelder post https://stackoverflow.com/questions/2077283/escape-special-html-characters-in-python
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))


def format_comment(comment):
    '''Utililty to strip non-alphanumeric code.'''
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ \
                    0123456789')
    comment = ''.join(filter(whitelist.__contains__, comment))


def search_comments(video_id=video_id):
    '''Searches YouTube Data API v3 for comments based on video id.'''
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    for video_id in video_id_list:
        video_comments = {}
        results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText",
        ).execute()
        video_comments['video_id'] = video_id
        comments = []
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment.encode('utf-8'))
        video_comments['comments'] = comments    
        print(video_comments, '\n')
    

if __name__ == '__main__':
    search_comments()