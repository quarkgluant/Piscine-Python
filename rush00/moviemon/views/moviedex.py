from django.shortcuts import render

def moviedex(request, id=None, param=None):
    return render(request, "moviemon/home.html")