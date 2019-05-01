from rest_framework import serializers

from songs.models import Song

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = (
			'id',
			#'slug',
			'songs',
			'mood',
			'video_id',
			#'song_embed_code',
			'recommendation_one',
			'recommendation_two',
			'recommendation_three',
			'recommendation_four',
			'recommendation_five'
		)
		#lookup_field = 'slug'







