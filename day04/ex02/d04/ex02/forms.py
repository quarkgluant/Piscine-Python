from django import forms

class myform(forms.Form):
	"""classe creation de formulaire"""
	my_text = forms.CharField(required = True)