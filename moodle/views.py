from django.shortcuts import render, redirect, get_object_or_404
from .models import Course,Message
from . import forms
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


'''Not a view, just a helper function'''
def student(request):
	return request.user.groups.filter(name='Student').exists()
	

def is_professor(user):
	return 'Professor' == user.groups.all()[0].name

def is_student(user):
	return 'Student' == user.groups.all()[0].name

@login_required
def home(request):
	'''Home page'''
	return render( request, 'home.html' , context = { 'courses':courses , 'student':student(request),})


@login_required
@user_passes_test(is_student,'home','')
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
		messages= Message.objects.filter(course=course)
		return render(request, 'course_enrolled.html',context = {'course':course,'student':student(request),'messages':messages})
	
	else:
		return render(request, 'course_to_enroll.html', context = {'course':course,'students':course.student.all().count(),'student':student(request)})
			

@login_required
@user_passes_test(is_student,'home','')
def courseEnroll(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	course.student.add(request.user)
	course.save()
	
	return redirect( 'course-detail', course.name)
	

@login_required	
@user_passes_test(is_student,'home','')
def courseDrop(request,pk):
	course = get_object_or_404(Course,pk=pk)
	
	course.student.remove(request.user)
	course.save()
	
	return redirect( 'course-detail', course.name)

@login_required	
@user_passes_test(is_professor,'home','')
def courseDelete(request,pk):
	course=get_object_or_404(Course,pk=pk)
	course.delete()
	
	return redirect('new-course')


@login_required
@user_passes_test(is_professor,'home','')
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
