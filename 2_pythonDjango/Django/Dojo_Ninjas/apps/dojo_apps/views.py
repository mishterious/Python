from django.shortcuts import render, HttpResponse, redirect
from models import *
# the index function is called when root is visited


def index(request):
    print "123456432134565432456754"

    Dojo.objects.create(first_name="Jeff", last_name="Bezos", email_address="bezos@amazon.com", age=5)

    


    return render(request,'dojo_apps/index.html')
