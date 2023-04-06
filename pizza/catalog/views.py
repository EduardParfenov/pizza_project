from django.shortcuts import render
from .models import Pizza, Salesman, Order

def index(request):
    num_pizzas = Pizza.objects.all().count()
    num_salesmans = Salesman.objects.all().count()
    num_orders = Order.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
    context = {
        'num_pizzas': num_pizzas,
        'num_orders': num_orders,
        'num_salesmans': num_salesmans,
        'num_visits': num_visits,
        },
    )


from django.views import generic

class PizzaListView(generic.ListView):
    model = Pizza
    paginate_by = 3  #  для пагинации

class PizzaDetailView(generic.DetailView):
    model = Pizza


class OrderListView(generic.ListView):
    model = Order


class SalesmanListView(generic.ListView):
    model = Salesman

