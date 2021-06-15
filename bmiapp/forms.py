from django import forms

class UserForm(forms.Form):
	tall = forms.CharField(label='身長(cm)', max_length=5)
	weight = forms.CharField(label='体重(kg)', max_length=5)