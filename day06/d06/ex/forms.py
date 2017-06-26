from django import forms
from django.contrib import auth
from .models import MyUser

class SignUpForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput)
	password_verif = forms.CharField(widget=forms.PasswordInput)

class SignInForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('username', 'password')


