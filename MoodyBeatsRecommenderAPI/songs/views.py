from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Song

class SongListView(ListView):
	model = Song
	template_name = 'songs/list_view.html'

class SongDetailView(DetailView):
	queryset = Song.objects.all()



