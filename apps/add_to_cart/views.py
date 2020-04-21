from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'add_to_cart/index.html')

def add(request):
    if request.method == "POST":
        request.session['quantity'] = int(request.POST['quantity'])
        request.session['product_id'] = request.POST['product_id']
        if request.session['product_id'] == '1015':
            total = request.session['quantity'] * 338.99
            request.session['total'] += total
        if request.session['product_id'] == '1016':
            total = request.session['quantity'] * 199.99
            request.session['total'] += total
        if 'order' not in request.session:
            request.session['order'] = []
            request.session['total'] = 10
        else:
            order = {
                'quantity': request.session['quantity'],
                'pruduct': request.session['product_id'],
                'total': request.session['total']
            }
            request.session['order'].append(order)

    print("8" * 50)
    print(request.session['order'])
    print("8" * 50)
    print(request.session['total'])
    print("8" * 50)

    print("8" * 50)

    return redirect('/show_cart')

def show_cart(request):

    return render(request, "add_to_cart/cart.html")

def clear_cart(request):
    request.session['order'] = []
    request.session['total'] = 0
    return render(request, "add_to_cart/cart.html")
