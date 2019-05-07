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
			'recommendation_one_link',
			'recommendation_two',
			'recommendation_two_link',
			'recommendation_three',
			'recommendation_three_link',
			'recommendation_four',
			'recommendation_four_link',
			'recommendation_five',
			'recommendation_five_link',
		)
		#lookup_field = 'slug'







