from django.shortcuts import render, redirect
from django.conf import settings
import random
from django.core.cache import cache
from ex.forms import SignUpForm, SignInForm
from ex.models import MyUser
import psycopg2

def index(request):
    if 'mycookie' in request.COOKIES:  #request.COOKIES est un dictionnaire : {'mycookie': 'Bob'}
        username = request.COOKIES['mycookie']
        response = render(request, 'ex/application.html', {'username': username})
    else:
        username = random.choice(settings.NAMES)
        request.COOKIES['mycookie'] = username
        response = render(request, 'ex/application.html', {'username': username})
        response.set_cookie('mycookie', username, max_age=settings.SESSION_COOKIE_AGE)

    return response

    # username = random.choice(settings.NAMES)
    # cache.set('username', username, 5)
    # username = cache.get('username')
    # print("username", cache.get('username'))
    # print(locals())
    # # if request.method == 'GET':
    # if cache.get('username') != None:
    #     return render(request,  "ex00/application.html", { 'username': username } )
    # else:
    #     cache.set('username', random.choice(settings.NAMES), 5)
    #     # username = request.POST.get('text', None)
    #     username = cache.get('username')
    #     # Settings the cookie in the request to pass it to the template engine
    #     return  redirect('index' )

                    # Set the value in the response as cookie
                # response.set_cookie('mycookie', cookie,
                #         max_age=settings.SESSION_COOKIE_AGE)

        # If the page is just refresh
    # return render(request,  "ex00/application.html", { 'username': username } )
    

def sign_in(request):
    users = MyUser.objects.all()
    if (request.method == "POST"):
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignInForm()
        else:
            form =  SignInForm()
        return render(request, 'ex/form.html', {'users' : users,
                                            'form': form })

def sign_up(request):
    if (request.method == "POST"):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_verif = form.cleaned_data["password_verif"]
            if password == password_verif:
                user = auth.authenticate(username=username, 
                                        password=password) 
                if user and user.is_active:  # Si l'objet renvoyé n'est pas None,  par défaut is_active est False
                    auth.login(request, user)  # nous connectons l'utilisateur
                else: # sinon une erreur sera affichée
                    form._errors["username"] = ["This user doesn't exist."]
            else:
                form._errors["password"] = ["les mots de passe ne sont pas semblables"]
    else:
        form = SignUpForm()
    return render(request, 'ex/form.html', {'form': form })
