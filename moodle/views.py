from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.


'''Not a view, just a helper function'''
def student(request):
	return request.user.groups.filter(name='Student').exists()
	
	
@login_required
def home(request):
	'''Home page'''
	return render( request, 'home.html' , context = { 'courses':courses , 'student':student(request) })


@login_required
def courses(request):
	'''Page with all the courses in which student has enrolled'''
	
	courses= Course.objects.filter(student__username=request.user.username)
	return render( request, 'courses.html' , context = {'courses':courses,'student':student(request)} )
	

@login_required	
def allcourses(request):
	courses=Course.objects.all()
	return render(request, 'allcourses.html',context = {'courses':courses,'student':student(request)})
	

@login_required	
def courseDetail(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	if request.user in course.student.all():

		return render(request, 'course_enrolled.html',context = {'course':course,'student':student(request)})
	
	else:
		return render(request, 'course_to_enroll.html', context = {'course':course,'students':course.student.all().count(),'student':student(request)})
			

@login_required
def courseEnroll(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	course.student.add(request.user)
	course.save()
	
	return redirect( 'course-detail', course.name)
	

@login_required	
def courseDrop(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	course.student.remove(request.user)
	course.save()
	
	return redirect( 'course-detail', course.name)
	

@login_required	
def courseDelete(request,pk):
	course=get_object_or_404(Course,pk=pk)
	course.delete()
	
	return redirect('new-course')


@login_required
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
	return render( request, 'new_course.html',context = {'form':form,'student':student(request)})
