from django.contrib import admin

from .models import Salesman, Order, Pizza

# admin.site.register(Salesman)
admin.site.register(Order)
admin.site.register(Pizza)

class SalesmanAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'time_open', 'time_close')
    fields = ['first_name', 'last_name', ('time_open', 'time_close')]

admin.site.register(Salesman, SalesmanAdmin)