# news/tasks.py

import requests
from django.utils import timezone
from .models import News, Category

def fetch_news():
    api_key = 'YOUR_NEWSAPI_KEY'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    response = requests.get(url)
    articles = response.json().get('articles', [])
    
    for article in articles:
        category, _ = Category.objects.get_or_create(name=article['source']['name'])
        News.objects.create(
            title=article['title'],
            description=article['description'],
            url=article['url'],
            published_at=timezone.now(),
            category=category
        )
