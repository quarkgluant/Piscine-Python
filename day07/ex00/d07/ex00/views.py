from django.shortcuts import HttpResponse, render, redirect
from ex00.models import Article, UserFavouriteArticle
from django.views.generic import TemplateView, ListView, FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm

class HomeView(TemplateView):
    # pattern_name = '/articles'
    model = Article
    template_name = "ex00/articles_list.html"

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "ex00/login.html"
    success_url = "/"

class ArticlesView(ListView):
    model = Article
    template_name = "ex00/articles_list.html"


