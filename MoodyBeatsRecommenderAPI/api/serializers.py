from rest_framework import serializers

from songs.models import (
	Song,
	Tag,
	NewVideo,
	NewComment,
	NewVideoTag,
	NewVideoStats,
	NewVideoCorrectMood,
)

class NewVideoStatsSerializer(serializers.ModelSerializer):
	new_video = serializers.StringRelatedField()
	class Meta:
		model = NewVideoStats
		fields = [
			'video_id',
			'video_view_count',
			'video_like_count',
			'new_video',
		]



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

class NewVideoTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewVideoTag
		fields = [
			'topics',
		]

class NewVideoSerializer(serializers.ModelSerializer):
	new_video_tags = NewVideoTagSerializer(many=True)

	class Meta:
		model = NewVideo
		fields = [
			'video_title',
			'video_id',
			'moods',
			'new_video_tags',
		]

class NewVideoDetailSerializer(serializers.ModelSerializer):
	new_video_tags = NewVideoTagSerializer(many=True)

	class Meta:
		model = NewVideo
		depth=3
		fields = [
			'video_id',
			'video_title',
			'moods',
			'new_video_tags',
		]

class NewVideoCorrectMoodSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewVideoCorrectMood
		fields = [
			'video_id',
			'video_title',
			'correct_moods',
		]



class NewCommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewComment
		fields = '__all__'

"""
class NewVideoStatsDetailSerializer(serializers.ModelSerializer):
	new_video_stats = NewVideoStatsSerializer(many=True)

	class Meta:
		model = NewVideoStats
		fields = [
			'new_video_stats',
		]
"""









