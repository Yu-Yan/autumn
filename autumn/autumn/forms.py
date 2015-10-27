from django import forms


class registerFrom(forms.Form):
	username = forms.CharField(max_length=50)
	email = forms.EmailField()
	password = forms.CharField(max_length=15, widget=forms.PasswordInput())
	name = forms.CharField(max_length=50)
	sig = forms.CharField(max_length=150, label='Signature')

class loginForm(forms.Form):
	username = forms.CharField(max_length=50, label='Username')
	password  = forms.CharField(max_length=15, widget=forms.PasswordInput(),label='Password')

class inputForm(forms.Form):
	title = forms.CharField(max_length=150)
	sub_title = forms.CharField(max_length=255)
	content = forms.CharField(widget=forms.Textarea())

class commentForm(forms.Form):
	content = forms.CharField(max_length=255)

class messageForm(forms.Form):
	content = forms.CharField(max_length=255)
