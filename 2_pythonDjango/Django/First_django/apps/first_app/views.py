from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# the index function is called when root is visited


# def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time_apps/page.html', context)


