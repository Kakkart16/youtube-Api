from celery import shared_task
from googleapiclient.discovery import build
from .models import Video
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

API_KEYS = ['key1', 'key2', 'key3']

@shared_task
def fetch_youtube_videos():
    # All the videos in the last 1 year.
    published_after = (datetime.utcnow() - timedelta(days=120)).isoformat() + 'Z'
    for key in API_KEYS:
        try:
            youtube_service = build('youtube', 'v3', developerKey=key)
            request = youtube_service.search().list(
                part='snippet',
                q='football',
                type='video',
                order='date',
                publishedAfter=published_after,
                maxResults=100
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
            break  
        except Exception as e:
            print(f"Error fetching videos with key {key}: {e}")
            if 'quotaExceeded' in str(e):
                continue
            else:
                raise 