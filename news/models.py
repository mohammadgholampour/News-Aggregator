# news/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(unique=True)
    published_at = models.DateTimeField()
    category = models.ForeignKey(Category, related_name='news', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

# سیگنال‌ها را بعد از تعریف مدل‌ها اضافه کنید
@receiver(post_save, sender=News)
def send_notification(sender, instance, created, **kwargs):
    if created:
        print(f"New article added: {instance.title}")
