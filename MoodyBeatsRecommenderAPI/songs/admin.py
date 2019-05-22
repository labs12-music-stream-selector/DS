from django.contrib import admin

# Register your models here.
from .models import Song, Tag, NewVideo, NewVideoTag

class SongModelAdmin(admin.ModelAdmin):
	models = Song 
	prepopulated_fields = {'slug': ('songs',)}

admin.site.register(Song, SongModelAdmin)

admin.site.register(Tag)



class NewVideoModelAdmin(admin.ModelAdmin):
    class Meta:
        model = NewVideo
    list_display = [
        'id',
        'video_id',
        'video_title',
        'moods',
        'video_view_count',
        'video_like_count',
        'video_favorite_count',
        'video_comment_count',
    ]
    list_editable = [
        'moods',
    ]
    list_display_links = ['video_title']
    search_fields = ['video_title', 'id', 'video_id']



admin.site.register(NewVideo, NewVideoModelAdmin)
admin.site.register(NewVideoTag)