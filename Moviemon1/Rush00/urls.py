from django.conf.urls import url

from . import views

urlpatterns = [
	# url('^Form', views.Form),
	url(r'^options/load_game', views.OptionsLoad),
	url(r'^options/save_game', views.OptionsSave),
	url(r'^battle/(?P<moviemon_id>[-\w]+)/$', views.Battle),
	url(r'^worldmap', views.Worldmap),
	url(r'^options', views.Options),
	url(r'^moviedex/(?P<moviemon_id>[-\w]+)$', views.MoviedexDetail),
	url(r'^moviedex', views.Moviedex),
	# url(r'^New', views.New),
	url(r'^$', views.New),
]
