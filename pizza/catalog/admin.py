from django.contrib import admin

from .models import Salesman, Order, Pizza

admin.site.register(Salesman)
admin.site.register(Order)
admin.site.register(Pizza)

