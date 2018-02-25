from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
	"""Model representing a course"""
	name = models.CharField(max_length=6,primary_key=True)
	professor = models.CharField(User,null=False,max_length=100)
	student =models.ManyToManyField(User)

	def __str__(self):
		return self.name
