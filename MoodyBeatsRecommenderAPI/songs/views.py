from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Song

class SongListView(ListView):
	#model = Song
	template_name = 'songs/list_view.html'

	def get_queryset(self, *args, **kwargs):
		qs = Song.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(songs__icontains=query)|
				Q(mood__icontains=query)|
				Q(recommendation_one__icontains=query)|
				Q(recommendation_two__icontains=query)|
				Q(recommendation_three__icontains=query)|
				Q(recommendation_four__icontains=query)|
				Q(recommendation_five__icontains=query)
			)
		return qs
		
	

class SongDetailView(DetailView):
	queryset = Song.objects.all()



