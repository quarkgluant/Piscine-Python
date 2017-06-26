############################# Video 02 Nginx simple


brew install nginx 
# website.conf
server {
    listen 8001;

    location /django/ {
        autoindex on;
        alias /nfs/2013/v/vwonteco/Code/formation_python_djongo/d08/videos/02_Nginx_Simple/django_example/;
    }
    location / {
        autoindex on;
        alias /nfs/2013/v/vwonteco/Code/formation_python_django/d08/videos/02_Nginx_Simple/website/;
    }
}
# dans ~/.brew/etc/nginx/nginx
include  /nfs/2013/v/vwonteco/Code/formation_python_djongo/d08/videos/02_Nginx_Simple/website.conf

nginx

127.0.01:8001


############################# Video 4 STATIC Files

# settings.py
STATIC_URL = '/static/' # dans 'app, avec un sous-dossier du nom de l'app c'est mieux
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# urls.py
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)

> ./manage.py collectstatic  #copie tous les fichiers static dans les sous-dossiers des apps les fichiers static et les copie dans le fichier staticfiles



############################# Video 5 MEDIA Files

# settings.py
MEDIA_URL = '/media/' # dans 'app, avec un sous-dossier du nom de l'app c'est mieux
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# urls.py
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

# models.py
from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=40)
    file = models.FileField(upload_yo'files')
 
# views.py
from django.shortcuts import render
from .forms import FileForm
from .models import File

# Create your views here.
def home(request):
    files = File.objects.all()
        if request.method == 'POST' :
        form = FileForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
    else:
        form = FileForm()
return render(request, "main/home.html" , {'form' : form,   'files' : files})

# home.html
<!doctype html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="/static/main/css/style.css"/>
</head>
<body>
    <p>Submit your files here :</p >
    <form   method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>
    <ul>
    {% for file in files %}
        <li>
            <a href="{{ file.file.url }}" >
                {{ file.name }}
                </a>
        </li>
        {% empty %}
        No file yet.
        {% endfor %}
    </ul>
</body>
</html>


########################## video Nginx + uWSGI

# website.conf
upstream django_uwsgi {
    server unix:///nfs/2013/v/vmonteco/Code/formation_python_django/d08/videos/07_Nginx_+_UWSGI/example.sock;
}
server {
    listen 8002; 
    server_name 127.0.0.1; 
    charset utf-8;

    root /nfs/2013/v/vmonteco/Code/fonnation_python_django/d08/videos/07_Nginx_+_ullSGI/example;

    set $myroot $document_root;

    location /media {
        alias $myroot/mediafiles;
    }
    location /static {
        alias $myroot/staticfiles;
    }
    location / {
        uwsgi_pass django.uwsgi; 
        include uwsgi_params;
    }
}

#########
#!/bin/sh
uwsgi --ini example_uwsgi.ini