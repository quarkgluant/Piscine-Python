from django.contrib import admin
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = ['title', 'author', 'synopsis', 'content', ]

admin.site.register(Article, ArticleAdmin)
