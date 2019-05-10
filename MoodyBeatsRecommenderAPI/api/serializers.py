from rest_framework import serializers

from songs.models import (
	Song,
	Tag,
	NewVideo
)



class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'
	

class SongSerializer(serializers.ModelSerializer):
	api_tags = TagSerializer(many=True)

	class Meta:
		model = Song
		fields = (
			'id',
			#'slug',
			'songs',
			'mood',
			'api_tags',
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
		read_only_fields = (
			'id',
			#'slug',
			'songs',
			'mood',
			'api_tags',
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

class NewVideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewVideo
		fields = '__all__'









