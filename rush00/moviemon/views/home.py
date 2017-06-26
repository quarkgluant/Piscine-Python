from django.shortcuts import render

def home(request):
    title = "MovieMons"
    return render(request, 'moviemon/home.html', {"title": title})