from django import forms

class NewCourse(forms.Form):
	name=forms.CharField(required=True,label='Course Name')
	

class NewPost(forms.Form):
	title=forms.CharField(max_length=100,required=True,label='',widget=forms.TextInput(attrs={ 'placeholder':'Title','style':'width:100%;max-width:400px'}))
	content=forms.CharField(max_length =500, required =True,label='' ,widget=forms.Textarea(attrs={ 'placeholder':'Post', 'style':'resize:none;height:150px;width:100%;max-width:400px'}))
	 
