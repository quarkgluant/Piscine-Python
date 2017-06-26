from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import logging
from logging.handlers import RotatingFileHandler
from django.shortcuts import redirect
from django.utils import timezone

from . import form as Form

def index(request):
    return HttpResponse("Hello World !")

def base(request):
	return render(request, "base.html")

def django(request):
	return render(request, "django.html")

def affichage(request):
	return render(request, "affichage.html")

def templates(request):
	return render(request, "templates.html")


logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
file_handler = RotatingFileHandler('ex02/ex02.logs', 'a', 1000000, 1)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def test():
    print('hello')

def ex02(request):
    t = test
    if (request.method == 'POST'):
        form = Form.MyForm(request.POST)
        if form.is_valid():
            timezone.now()
            now = timezone.now()
            content = []
            logger.info(" {0}:{1} {2}/{3}/{4}".format(int(now.hour)+2, now.minute, now.day, now.month, now.year) + " " + form.cleaned_data['name'])
            with open('ex02/ex02.logs', 'r') as filecontent:
                for line in filecontent:
                    content.append(line)

            return render(request, 'ex02/form.html', {'form':form,'list_logs': content, 'callback':t })
    else:
        content = []
        with open('ex02/ex02.logs', 'r') as filecontent:
            for line in filecontent:
                content.append(line)
        form = Form.MyForm()


    return render(request, 'ex02/form.html', {'form':form, 'list_logs': content, 'callback':t })


def index(request):

	lst = list()
	now = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')

	if (request.method == 'POST'):
		form = MyForm(request.POST)
		if form.is_valid():
			with open(settings.MY_WAY, 'a') as f2:
				f2.write(now + " " + form.cleaned_data['my_text'] + "\n")

	form = MyForm()

	with open(settings.MY_WAY, 'r') as f:
		for line in f:
			lst.append(line)

	return render(request, "ex02/index.html", {'form' : form, 'liste' : lst})