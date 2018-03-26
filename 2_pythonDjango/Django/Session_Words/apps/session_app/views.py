# views.py
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    
    words = {"all_words": []}

    return render(request, "session_app/sessionword.html", words)


def load(request):
    if request.method == "POST":
        if 'obj' not in request.session: 
            request.session['obj'] = []
        if 'fonts' in request.POST: 
            obj = {
                'word': request.POST['name'],
                'color': request.POST['color'],
                'fonts': request.POST['fonts'],
                "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
            }
        else: 
            obj = {
                'word': request.POST['name'],
                'color': request.POST['color'],
                "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
            }

        request.session['obj'].append(obj)
        request.session.modified = True 

        print request.session['obj']

        return redirect('/')

