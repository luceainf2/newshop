from django.db import models


class Video(models.Model):
    likes = models.PositiveIntegerField(default=0)
    embed_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
