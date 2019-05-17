from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

from taggit.managers import TaggableManager




# Create your models here.
class Tag(models.Model):
	name = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name

class Song(models.Model):
	songs							= models.CharField(db_index=True, max_length=200, null=True, blank=True)
	tags 							= TaggableManager()
	# api_tags						= models.ManyToManyField('Song', related_name='tag_songs', null=True, blank=True)
	api_tags						= models.ManyToManyField(Tag)
	video_id						= models.CharField(max_length=11, null=True, blank=True)
	song_embed_code					= models.TextField(null=True, blank=True)
	mood 							= models.CharField(max_length=20, null=True, blank=True)
	slug 							= models.SlugField(max_length=200, unique=True)
	recommendation_one 				= models.CharField(max_length=140, null=True, blank=True)
	recommendation_one_link 		= models.URLField(null=True, blank=True)
	recommendation_one_embed_code	= models.TextField(null=True, blank=True)
	recommendation_two 				= models.CharField(max_length=140, null=True, blank=True)
	recommendation_two_link 		= models.URLField(null=True, blank=True)
	recommendation_two_embed_code	= models.TextField(null=True, blank=True)
	recommendation_three 			= models.CharField(max_length=140, null=True, blank=True)
	recommendation_three_link 		= models.URLField(null=True, blank=True)
	recommendation_three_embed_code	= models.TextField(null=True, blank=True)
	recommendation_four 			= models.CharField(max_length=140, null=True, blank=True)
	recommendation_four_link 		= models.URLField(null=True, blank=True)
	recommendation_four_embed_code	= models.TextField(null=True, blank=True)
	recommendation_five 			= models.CharField(max_length=140, null=True, blank=True)
	recommendation_five_link 		= models.URLField(null=True, blank=True)
	recommendation_five_embed_code	= models.TextField(null=True, blank=True)


	def __str__(self):
		return self.songs

	def get_absolute_url(self):
		return reverse("song:detail", kwargs={"pk":self.pk})


def create_slug(instance, new_slug=None):
	slug = slugify(instance.songs)
	if new_slug is not None:
		slug = new_slug
	qs = Song.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_song_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_song_receiver, sender=Song)




class NewVideoTag(models.Model):
	topics = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.topics

class NewVideo(models.Model):
	MOOD_CHOICES = (
	('HAPPY', 'Happy'),
	('IN-LOVE', 'In-Love'),
	('SAD', 'Sad'),
	('CONFIDENT-SASSY', 'Confident-sassy'),
	('CHILL', 'Chill'),
	('ANGRY', 'Angry'),
	)
	video_title 			= models.TextField(db_index=True, null=True, blank=True)
	video_id 				= models.CharField(max_length=11, null=False, blank=True, primary_key=True)
	# video_view_count 		= models.TextField(null=True, blank=True)
	# #video_like_count 		= models.IntegerField(null=True, blank=True)
	# video_favorite_count 	= models.TextField(null=True, blank=True)
	# video_comment_count 	= models.TextField(null=True, blank=True)
	moods 					= models.CharField(choices=MOOD_CHOICES, max_length=20,  default='HAPPY')
	new_video_tags 			= models.ManyToManyField(NewVideoTag)
	#updated					= models.DateTimeField(auto_now=True)
	#timestamp				= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.video_title

class NewVideoStats(models.Model):
	video_id				= models.CharField(max_length=11, null=True, blank=True, unique=True)
	video_view_count 		= models.CharField(max_length=15, null=True, blank=True)
	video_like_count 		= models.CharField(max_length=15, null=True, blank=True)
	video_favorite_count 	= models.CharField(max_length=15, null=True, blank=True)
	video_comment_count 	= models.CharField(max_length=15, null=True, blank=True)

	new_video 				= models.ForeignKey(NewVideo, on_delete=models.CASCADE)

	#def __str__(self):
		#return self.new_video

class NewVideoCorrectMood(models.Model):
	MOOD_CHOICES = (
	('HAPPY', 'Happy'),
	('IN-LOVE', 'In-Love'),
	('SAD', 'Sad'),
	('CONFIDENT-SASSY', 'Confident-sassy'),
	('CHILL', 'Chill'),
	('ANGRY', 'Angry'),
	)
	video_id				= models.CharField(max_length=11, null=True, blank=True)
	video_title				= models.TextField(null=True, blank=True)
								# video_id cannot be unique since we'll get repeated corrected moods for each video_id
	correct_moods 			= models.CharField(choices=MOOD_CHOICES, max_length=20,  default='UNKNOWN')

	def __str__(self):
		return self.video_title



class NewComment(models.Model):
	video_id = models.CharField(max_length=11, null=True, blank=True, unique=True)
	comments = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.video_id




	
	





