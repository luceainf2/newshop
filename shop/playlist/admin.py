from django.contrib import admin

from playlist.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'embed_code', 'created_at')