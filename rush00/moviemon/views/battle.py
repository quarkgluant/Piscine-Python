from django.shortcuts import render

def battle(request, id=None, param=None):
    return render(request, "moviemon/home.html")