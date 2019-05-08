'''
This module returns data from the YouTube Data API v3, using parameters
from https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.search.list
'''

from dotenv import load_dotenv
from googleapiclient.discovery import build
import os

load_dotenv()


def main():
    api_service_name = 'youtube'
    api_version = 'v3'
    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')

    youtube = build(api_service_name, api_version,
                    developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part='id,snippet',
        maxResults=10,
        q='instrumental',
        relevanceLanguage='en',
        type='video',
        videoDuration='medium',
        videoLicense='creativeCommon',
    ).execute()

    videos = []
    result_count = 0

    for search_result in request.items():
        print('search_result', result_count, ': ', search_result)
        result_count += 1
        # videos.append('{} ({})'.format(request['item']['snippet']['title'],
        #                                request['item']['id']['videoId']))
    

    # print('Videos:\n', '\n'.join(videos))
    # return videos


if __name__ == '__main__':
    main()
