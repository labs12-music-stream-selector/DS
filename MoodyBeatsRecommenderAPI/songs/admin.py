from django.contrib import admin

# Register your models here.
from .models import (
	Song,
	Tag,
	NewVideo,
	NewComment,
	NewVideoTag,
	NewVideoStats,
	NewVideoCorrectMood,
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
		#'id',
		'video_id',
		'video_title',
		'moods',
		#'video_view_count',
		#'video_like_count',
		#'video_favorite_count',
		#'video_comment_count',
		#'timestamp',
		#'updated',
	]
	list_editable = [
		'moods',
	]
	list_display_links = ['video_title']
	search_fields = ['video_title', 'video_id']

admin.site.register(NewVideo, NewVideoModelAdmin)

class NewVideoStatsModelAdmin(admin.ModelAdmin):
	class Meta:
		model = NewVideoStats
	list_display = [
		'video_id',
		'video_view_count',
		'video_like_count',
		'video_favorite_count',
		'video_comment_count',
		'new_video',
	]
	list_display_links = [
		'new_video',
	]

admin.site.register(NewVideoStats, NewVideoStatsModelAdmin)

class NewVideoCorrectMoodModelAdmin(admin.ModelAdmin):
	class Meta:
		model = NewVideoCorrectMood
	list_display = [
		'video_id',
		'video_title',
		'correct_moods',
	]
	search_fields = [
		'video_id',
		'video_title',
	]

admin.site.register(NewVideoCorrectMood, NewVideoCorrectMoodModelAdmin)

class NewCommentModelAdmin(admin.ModelAdmin):
	class Meta:
		NewComment
	list_display = [
		'video_id',
		'comments',
	]

admin.site.register(NewComment, NewCommentModelAdmin)

admin.site.register(NewVideoTag)



