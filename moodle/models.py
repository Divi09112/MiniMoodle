from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
	"""Model representing a course"""
	name = models.CharField(max_length=6,primary_key=True)
	professor = models.OneToOneField(User,blank=False,null=False,on_delete=models.CASCADE,related_name="+")
	student =models.ManyToManyField(User,null=True,blank=True)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('course-detail',args=[str(self.name)])
