from django.contrib import admin

# Register your models here.
from .models import Song, Tag

class SongModelAdmin(admin.ModelAdmin):
	models = Song 
	prepopulated_fields = {'slug': ('songs',)}

admin.site.register(Song, SongModelAdmin)

admin.site.register(Tag)

