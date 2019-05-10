from django.contrib import admin

# Register your models here.
from .models import Song, Tag, NewVideo

class SongModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Song
	list_display = [
		"songs",
		"video_id",
		"mood",
	]
	list_filter = ["mood"]
	list_editable = ["mood", "video_id",]
	search_fields = ["songs", "mood"]

	prepopulated_fields = {'slug': ('songs',)}



admin.site.register(Song, SongModelAdmin)

admin.site.register(Tag)

admin.site.register(NewVideo)




