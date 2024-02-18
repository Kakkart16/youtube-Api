from celery import shared_task
from googleapiclient.discovery import build
from .models import Video
from datetime import datetime, timedelta

key='AIzaSyBNPQab5YWKiOWdxeoRB_qqPBAeBPaoH-s'

@shared_task
def sike():
    print('hello')

@shared_task
def fetch_youtube_videos():
    print('Data Fetched')
    # All the videos in the last 1 year.
    published_after = (datetime.utcnow() - timedelta(days=365)).isoformat() + 'Z'
    youtube_service = build('youtube', 'v3', developerKey=key)
    request = youtube_service.search().list(
        part='snippet',
        q = 'football',
        type = 'video',
        order = 'date',
        publishedAfter = published_after,
        maxResults = 100
    )
    response = request.execute()
    videos = response.get('items', [])

    for item in videos:
        video = Video(
            title=item['snippet']['title'],
            description=item['snippet']['description'],
            published_datetime=item['snippet']['publishedAt'],
            thumbnail_url=item['snippet']['thumbnails']['default']['url']
        )
        video.save()
    
        