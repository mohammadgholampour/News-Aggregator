# news/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import News

@receiver(post_save, sender=News)
def send_notification(sender, instance, created, **kwargs):
    if created:
        print(f"New article added: {instance.title}")
