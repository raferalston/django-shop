from .models import ItemArticle
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

@receiver(post_save, sender=ItemArticle)
def news_save_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} saved.")


@receiver(post_delete, sender=ItemArticle)
def news_delete_handler(sender, **kwargs):
    if settings.DEBUG:
        print(f"{kwargs['instance']} deleted.")
