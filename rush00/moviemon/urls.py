from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^worldmap/$', worldMap, name='worldmap'),
    url(r'^worldmap/(?P<param>up|down|left|right|a)/$', worldMap, name='worldmap'),

    url(r'^battle/(?P<id>[0-9]+)/(?P<param>a|b)/', worldMap, name="battle"),

    url(r'^moviedex/(?P<id>[0-9]+)/(?P<param>b)/$', worldMap, name='worldmap'),
    url(r'^moviedex/(?P<param>up|down|left|right|a|select)/$', worldMap, name='worldmap'),

    url(r'^options/$', options, name='options'),
    url(r'^options/(?P<param>a|b|start)/$', options, name='options'),
    url(r'^options/save_game/(?P<param>up|down|left|right|a|b)/$', optionsSaveGame, name='options'),
    url(r'^options/load_game/(?P<param>up|down|left|right|a|b)/$', optionsLoadGame, name='options'),
]