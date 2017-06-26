from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import psycopg2

# Create your views here.
def init(request):
    try:
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
            )
        curr = conn.cursor()

        curr.execute(""" CREATE TABLE IF NOT EXISTS ex04_movies (
            title varchar(64) UNIQUE NOT NULL,
            episode_nb serial PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            """)
        conn.commit()
        conn.close()
        return HttpResponse("OK")
    except psycopg2.Error as e:
        return HttpResponse("problemo! : {}".format(e.pgerror))

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
    try:
        movies = (
            {'title': 'The Phantom Menace', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '1999-05-19'},
            {'title': 'Attack of the Clones', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2002-05-16'},
            {'title': 'Revenge of the Sith', 'director': 'George Lucas', 'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
            {'title': 'A New Hope', 'director': 'George Lucas', 'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},
            {'title': 'The Empire Strikes Back', 'director': 'Irvin Kershner', 'producer': 'Gary Kutz, Rick McCallum', 'release_date': '1980-05-17'},
            {'title': 'Return of the Jedi', 'director': 'Richard Marquand','producer':  'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},
            {'title': 'The Force Awakens', 'director': 'J. J. Abrams', 'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'},
        )
        conn = psycopg2.connect(
            database='formationdjango',
            host='localhost',
            user='djangouser',
            password='secret'
            )
        curr = conn.cursor()

        ret = []
        for movie in movies:
            try:
                print("""('{0}', "{1}", "{2}", "{3}" )""".format(movie['title'], movie['director'], movie['producer'], movie['release_date']))
                curr.execute(""" INSERT INTO ex04_movies (title, director, producer, release_date) VALUES (%s, %s, %s, %s)
            """, (movie['title'], movie['director'], movie['producer'], movie['release_date']))
            #     print("""("{0}", "{1}", "{2}", "{3}" )""".format(movie['title'], movie['director'], movie['producer'], movie['release_date']))
            #     curr.execute(""" INSERT INTO ex02_movies (title, director, producer, release_date) VALUES (%s, %s, %s, %s)
            # ('{0}', '{1}', '{2}', '{3}')
            # """.format(movie['title'], movie['director'], movie['producer'], movie['release_date']))
                conn.commit()
                ret.append("OK<br>")
            except psycopg2.Error as e:
                return HttpResponse(" Problème Avec le film {} : {}".format(movie['title'], e.pgerror))
        return HttpResponse(ret)
    except psycopg2.Error as e:
        HttpResponse("problemo! : {}".format(e.pgerror))
        

def display(request):
    try:
        conn = psycopg2.connect(
                database='formationdjango',
                host='localhost',
                user='djangouser',
                password='secret'
            )

        curr = conn.cursor()

        curr.execute(""" SELECT * FROM ex04_movies """)
        response = curr.fetchall()
        data = []
        for row in response:
            data.append(row)
        conn.close()
        if data == []:
            raise Exception ()
        return render(request, "ex04/display.html", {'data' : data})
    except Exception as e:
        return HttpResponse("No data available")

def remove(request):
    try:
        conn = psycopg2.connect(
                database='formationdjango',
                host='localhost',
                user='djangouser',
                password='secret'
            )

        curr = conn.cursor()

        # if some data is send
        if request.method == 'POST':
            form = request.POST
            print(form)
            curr.execute(" DELETE FROM ex04_movies WHERE episode_nb = %s", [int(form['movies'][1:].replace('"', ''))])
            conn.commit()

                
        curr.execute(""" SELECT * FROM ex04_movies """)        
        response = curr.fetchall()
        data = []
        for row in response:
            dat = (row[0], row[1])
            print(row[0], row[1])
            data.append(dat)
        conn.close()
        
        if data == []:
            raise Exception ()
        return render(request, "ex04/form_to_del.html", {'data' : data})
    except Exception as e:
        return HttpResponse("No data available")        

