from django.db import models
from django.contrib.auth.models import User
class Challenge(models.Model):
	challengeName = models.CharField(max_length=100)
	challengeDescription = models.TextField(default = "")
	challengeOwner = models.ForeignKey(User)
	challengeParticipants = models.ManyToMany(User)
	def __unicode__(self):
		return unicode(self.id)

class Cateogry(models.Model):
	categoryName = models.CharField(max_length = 100)
	categoryDescription = models.TextField(default = "")
	def __unicode__(self):
		return unicode(self.categoryName)

class Question(models.Model):
	


