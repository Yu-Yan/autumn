from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

# Create your models here.

#model for author, using onetoonefield to link user object
class Author(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=50)
	sig = models.CharField(max_length=150)
	up_num = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username

class Blog(models.Model):
	title = models.CharField(max_length=150)
	sub_title = models.CharField(max_length=255)
	pub_date = models.DateField(auto_now=True)
	author = models.ForeignKey(Author)
	content = models.TextField()
	up_num = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	author = models.ForeignKey(Author)
	blog = models.ForeignKey(Blog)
	content = models.CharField(max_length=255)
	pub_date = models.DateField(auto_now=True)

class Message(models.Model):
	author = models.ForeignKey(Author)
	to_author = models.ForeignKey(Author, related_name='message_to')
	content = models.CharField(max_length=255)
	pub_date = models.DateField(auto_now=True)