'''
This module returns data from the YouTube Data API v3, using parameters
from https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.search.list
'''

from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

load_dotenv()


def html_reverse_escape(string):
    '''Reverse escapes HTML code in string into ASCII text.'''
    # see Ned Batchelder post https://stackoverflow.com/questions/2077283/escape-special-html-characters-in-python
    return (string \
        .replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"'))


def main():
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part='id,snippet',
        maxResults=10,
        order='date',
        q='instrumental',
        relevanceLanguage='en',
        type='video',
        videoDuration='medium',
        videoLicense='creativeCommon',
    ).execute()

    videos = []
    result_count = 0

    for search_result in request['items']:
        video_title = search_result['snippet']['title']  # .replace("&quot;", '"')
        video_title = html_reverse_escape(video_title)
        video_id = search_result['id']['videoId']
        try:
            # print('search_result', result_count, ':') 
            # print(video_title)
            # print('video_id is:', video_id, '\n')
            videos.append((video_title, video_id))
        except UnicodeError as e:
            print('Unicode error prevented printing', result_count, '\n')
            result_count += 1
            continue
        result_count += 1
    

    for video in videos:
        try:
            print(video)
        except UnicodeError:
            print('Unicode error prevented printing a video.\n')
            continue
    return videos


if __name__ == '__main__':
    main()
