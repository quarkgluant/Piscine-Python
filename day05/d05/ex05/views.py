from django.shortcuts import render
from django.http import HttpResponse
from django.db import *
from .models import Movies
# Create your views here.

def populate(request):
#   ◦ episode_nb : 1 - title : The Phantom Menace - director : George Lucas -
# producer : Rick McCallum - release_date : 1999-05-19
# ◦ episode_nb : 2 - title : Attack of the Clones - director : George Lucas - producer
# : Rick McCallum - release_date : 2002-05-16
# ◦ episode_nb : 3 - title : Revenge of the Sith - director : George Lucas - producer :
# Rick McCallum - release_date : 2005-05-19
# ◦ episode_nb : 4 - title : A New Hope - director : George Lucas - producer : Gary
# Kurtz, Rick McCallum - release_date : 1977-05-25
# ◦ episode_nb : 5 - title : The Empire Strikes Back - director : Irvin Kershner -
# producer : Gary Kutz, Rick McCallum - release_date : 1980-05-17
# ◦ episode_nb : 6 - title : Return of the Jedi - director : Richard Marquand - producer
# : Howard G. Kazanjian, George Lucas, Rick McCallum - release_date :
# 1983-05-25
# 11
# D05 - Formation Python-Django Django - ORM
# ◦ episode_nb : 7 - title : The Force Awakens - director : J. J. Abrams - producer :
# Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date : 2015-12-11

    movies = (
        {'episode_nb': 1, 'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
        {'episode_nb': 2, 'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
        {'episode_nb': 3, 'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
        {'episode_nb': 4, 'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
        {'episode_nb': 5, 'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kutz, Rick McCallum', 'release_date': '1980-05-17'},
        {'episode_nb': 6, 'title': 'Return of the Jedi', 'director': 'Richard Marquand','producer':  'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
        {'episode_nb': 7, 'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'}
    )
    ret = []
    for movie in movies:
        try:            
            m = Movies(
                title=movie['title'], 
                director=movie['director'], 
                producer=movie['producer'], 
                release_date=movie['release_date']
            )
            m.save()
            ret.append("OK<br>")
        except Exception as e:
            ret.append(" Problème: {}<br>".format(e))
    # movies =  Movies.objects.all()
    # for movie in movies:
    #     print("movie: {} {} {} {} {}".format(movie.episode_nb, movie.title, movie.director, movie.producer, movie.release_date ))
    
    return HttpResponse(ret)

 
def display(request):

        movies =  Movies.objects.all()
        print("movies: {}".format(movies))
        # print("longueur: {}".format(response.len))
        data = []
        for movie in movies:
            data.append((movie.episode_nb, movie.title, movie.opening_crawl, movie.director, movie.producer, movie.release_date ))
            print("movie: {} {} {} {} {} {}".format(movie.episode_nb, movie.title, movie.opening_crawl, movie.director, movie.producer, movie.release_date ))
        print(data)
        if data == []:
            return HttpResponse("No data available")
        else:
            return render(request, "ex05/display.html", {'data' : data })

def remove(request):
    try:
        if (request.method == "POST"):
            form = request.POST
            m = Movies.objects.filter(episode_nb=int(form['movies'][1:].replace('"', '')))
            m.delete()
        data = []
        movies = Movies.objects.all()
        for movie in movies:
            data.append((movie.episode_nb, movie.title ))
            print("movie: episode no:{} titre:{} ".format(movie.episode_nb, movie.title ))
        print(data)
        if data == []:
            raise Exception ()
        return render(request, "ex05/form_to_del.html", {'data' : data })    
    except:            
        return HttpResponse("No data available")
