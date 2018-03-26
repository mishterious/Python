from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):

    Users.objects.create(first_name="Jeff", last_name="Bezos", email_address="bezos@amazon.com", age=59)
    
    print context
    return render(request, "assingment_apps/index.html", context)


def adduser(request):

    return redirect('/')