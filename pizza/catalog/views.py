from django.shortcuts import render
from .models import Pizza, Salesman, Order

def index(request):
    num_pizzas = Pizza.objects.all().count()
    num_salesmans = Salesman.objects.all().count()
    num_orders = Order.objects.all().count()

    return render(
        request,
        'index.html',
    context = {
        'num_pizzas': num_pizzas,
        'num_salesmans': num_salesmans,
        'num_orders': num_orders,
        },
    )