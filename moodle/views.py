from django.shortcuts import render, redirect
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
	
	if request.user in course.student.all():

		return render(request, 'course_enrolled.html',context={'course':course})
	
	else:
		students=0
		for student in course.student.all():
			students+=1 
		return render(request, 'course_to_enroll.html', context ={'course':course,'students':students})
			

def courseEnroll(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	course.student.add(request.user)
	course.save()
	
	return redirect( 'course-detail', course.name)
	
	
def courseDrop(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	course.student.remove(request.user)
	course.save()
	
	return redirect( 'course-detail', course.name)
