from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request):
    print "1298371924874939"
    if 'products' not in request.session:
        request.session['products'] = 0
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'bill' not in request.session:
        request.session['bill'] = 0
    if 'total_cost' not in request.session:
        request.session['total_cost'] = 0

    request.session['products'] = [
        {
            'product_id': 1,
            'name': 'Dojo T-shirt',
            'price': 19.99
        },
        {   
            'product_id': 2,
            'name': 'Dojo Sweater',
            'price': 29.99
        },
        {
            'product_id': 3,
            'name': 'Dojo Cup', 
            'price': 4.99
        },
        {
            'product_id': 4,
            'name': 'Algorithm Book',
            'price': 49.99
        }
    ]
    return render(request, "amadon/index.html")


def buy(request):
    for item in request.session['products']:
        print request.session['products']
        print request.session['total']
        print(item['product_id'], request.POST['product_id'])
        if item['product_id'] == float(request.POST['product_id']):
            request.session['total'] += int(request.POST['quantity'])
            request.session['bill'] = int(request.POST['quantity']) * float(item['price'])
            request.session['total_cost'] += float(request.session['bill'])
    return redirect(thankyou)


def thankyou(request):

    print "we're here +============================================="
    return render(request, "amadon/thankyou.html")