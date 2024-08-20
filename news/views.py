# news/views.py

from django.shortcuts import render
from .models import News, Category

def news_list(request):
    category_name = request.GET.get('category')
    if category_name:
        news_list = News.objects.filter(category__name=category_name).order_by('-published_at')
    else:
        news_list = News.objects.all().order_by('-published_at')
    categories = Category.objects.all()
    context = {
        'news_list': news_list,
        'categories': categories
    }
    return render(request, 'news/news_list.html', context)
