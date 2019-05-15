from django.contrib import admin

# Register your models here.
from .models import (
	Song,
	Tag,
	NewVideo,
	NewComment,
	NewVideoTag,
)

class SongModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Song
	list_display = [
		"id",
		"songs",
		"video_id",
		"mood",
	]
	list_display_links = ['songs']
	list_filter = ["mood"]
	list_editable = ["mood", "video_id",]
	search_fields = ["songs", "mood"]

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
	]
	list_editable = [
		'moods',
	]
	list_display_links = ['video_title']
	search_fields = ['video_title', 'id',]



admin.site.register(NewVideo, NewVideoModelAdmin)

class NewCommentModelAdmin(admin.ModelAdmin):
	class Meta:
		NewComment
	list_display = [
		'video_id',
		'comments',
	]

admin.site.register(NewComment, NewCommentModelAdmin)

admin.site.register(NewVideoTag)



