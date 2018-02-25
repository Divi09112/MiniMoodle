from django.shortcuts import render
from .models import Course
from django.views import generic

# Create your views here.

def home(request):
	'''Home page'''
	return render(request,'home.html',context={'courses':courses})

def courses(request):
	'''Page with all the courses in which student has enrolled'''
	courses= Course.objects.filter(student__username=request.user.username)
	return render( request, 'courses.html' , context={'courses':courses} )
	
def allcourses(request):
	courses=Course.objects.all()
	return render(request, 'allcourses.html',context={'courses':courses})
