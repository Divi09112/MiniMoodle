from django import forms

class NewCourse(forms.Form):
	name=forms.CharField(required="True",label='Course Name')
