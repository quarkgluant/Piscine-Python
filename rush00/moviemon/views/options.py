from django.shortcuts import render
from django.shortcuts import redirect

def options(request, param = None):

    if param == "a":
        return redirect('/save_game')
    elif param == "b":
        return redirect('/')
    elif param == "start":
        return redirect('/worldmap')
    return render(request, "moviemon/options.html")

def optionsSaveGame(request, param=None):
    if param == "up":
        return redirect('/save_game')
    elif param == "down":
        return redirect('/')
    elif param == "a":
        return redirect('/worldmap')
    elif param == "b":
        return redirect('/options')

    return render(request, "moviemon/save_game.html")

def optionsLoadGame(request, param=None):
    if param == "up":
        return redirect('/save_game')
    elif param == "down":
        return redirect('/')
    elif param == "left":
        return redirect('/worldmap')
    elif param == "right":
        return redirect('/')
    elif param == "a":
        return redirect('/worldmap')
    elif param == "b":
        return redirect('/')

    return render(request, "moviemon/options.html")