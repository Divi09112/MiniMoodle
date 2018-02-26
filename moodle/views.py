from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from . import forms

# Create your views here.

def home(request):
	'''Home page'''
	student=request.user.groups.filter(name='Student').exists()
	return render(request,'home.html',context={'courses':courses,'student':student})


def courses(request):
	'''Page with all the courses in which student has enrolled'''
	group=request.session.get('group',request.user.groups.all()[0])
	courses= Course.objects.filter(student__username=request.user.username)
	return render( request, 'courses.html' , context={'courses':courses,'group':group} )
	
	
def allcourses(request):
	group=request.session.get('group',request.user.groups.all()[0])
	courses=Course.objects.all()
	return render(request, 'allcourses.html',context={'courses':courses,'group':group})
	
	
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
	
	
def newCourse(request):
	if request.method=='POST':
		form=forms.NewCourse(request.POST)
		if form.is_valid():
			name=request.POST.get('name')
			
			course=Course(name=name,professor=request.user)
			course.save()
			
			return redirect('course-detail',course.name)
	else:
		form=forms.NewCourse()	
	return render( request, 'new_course.html',context={'form':form})
