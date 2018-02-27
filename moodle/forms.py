from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewCourse(forms.Form):
	name=forms.CharField(required=True,label='Course Name',widget=forms.TextInput(attrs={'maxlength':'6'}))
	limit = forms.IntegerField(required=True,label='Maximum Strength',widget=forms.NumberInput(attrs={'min':'1'}))


class NewPost(forms.Form):
	title=forms.CharField(max_length=100,required=True,label='',widget=forms.TextInput(attrs={ 'placeholder':'Title','style':'width:100%;max-width:400px'}))
	content=forms.CharField(max_length =500, required =True,label='' ,widget=forms.Textarea(attrs={ 'placeholder':'Post', 'style':'resize:none;height:150px;width:100%;max-width:400px'}))


GROUP_CHOICES=[
	('Professor','Professor'),
	('Student','Student'),
]


class NewUser(UserCreationForm):
	group=forms.CharField(required=True,widget=forms.Select(choices=GROUP_CHOICES,attrs={'default':None}))
	lname=forms.CharField(required=True)
	fname=forms.CharField(required=True)
	class Meta:
		model = User
		fields = ('username','fname','lname','password1','password2','group')
