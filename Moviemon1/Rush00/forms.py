from django import forms

class MyForm(forms.Form):
	email = forms.EmailField(required = True)
	name = forms.CharField(required = True)
