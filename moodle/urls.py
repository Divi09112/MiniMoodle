from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('courses/',views.courses,name='courses'),
	path('courses/(?P<pk>\d+)/',views.courseDetail,name='course-detail'),
	path('allcourses/',views.allcourses,name='allcourses'),
]
