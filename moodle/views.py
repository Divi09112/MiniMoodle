from django.shortcuts import render
from .models import Course
from django.views import generic
from django.shortcuts import get_object_or_404

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
	
	
def courseDetail(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	if course.student_set.filter(student=request.user.username).exists():
		return render(request, course_enrolled.html,context={'course':course})
