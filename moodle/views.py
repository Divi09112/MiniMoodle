from django.shortcuts import render
from .models import Course

# Create your views here.

def home(request):
	'''Home page'''
	courses=Course.objects.all()
	return render(request,'home.html',context={'courses':courses})

def courses(request):
	'''Page with all the courses in which student has enrolled'''
	courses= Course.objects.filter(student__username='stud1')
	return render( request, 'courses.html' , context={'courses':courses} )
