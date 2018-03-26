from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited


def index(request):
    print "123456432134565432456754"
    return render(request,'survey_app/survey.html')


def result(request):
    if request.method == "POST":
        print "We're here!!!!"
        print request.POST['myname']
        print "=============================================================="
        context = {
            "name": request.POST['myname'],
            "location": request.POST['location'],
            "language": request.POST['language'],
            "comment": request.POST['comment']
        }
        print context

        return render(request, 'survey_app/result.html', context)