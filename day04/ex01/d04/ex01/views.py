from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World !")

def base(request):
	return render(request, "base.html")

def django(request):
	return render(request, "django.html")

def affichage(request):
	return render(request, "affichage.html")

def templates(request):
	return render(request, "templates.html")