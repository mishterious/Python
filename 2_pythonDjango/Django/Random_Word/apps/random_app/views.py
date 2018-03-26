from django.shortcuts import render, HttpResponse, redirect s
from time import gmtime, strftime
from django.utils.crypto import get_random_string
# the index function is called when root is visited


def index(request):

    return render(request,'random_app/page.html')


def generate(request):
    context = {
        "random_string": get_random_string(length=14)
    }

    return render(request, 'random_app/page.html', context)