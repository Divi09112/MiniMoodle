from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('courses/',views.courses,name='courses'),
	url(r'^courses/(?P<pk>\w+)/$',views.courseDetail,name='course-detail'),
	path('allcourses/',views.allcourses,name='allcourses'),
]
