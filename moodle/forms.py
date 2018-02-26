from django import forms

class NewCourse(forms.Form):
	name=forms.CharField(required=True,label='Course Name')
	

class NewPost(forms.Form):
	title=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={ 'placeholder':'title'}))
	content=forms.CharField(max_length =500, required =True, widget=forms.TextInput(attrs={ 'placeholder':'post'}))
	 
