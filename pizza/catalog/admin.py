from django.contrib import admin
from .models import Salesman, Pizza, Order

# admin.site.register(Salesman)
admin.site.register(Order)
# admin.site.register(Pizza)


class SalesmanAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'time_open', 'time_close')   # страница Salesman
    fields = ['first_name', 'last_name', ('time_open', 'time_close')]       # страница add Salesman

admin.site.register(Salesman, SalesmanAdmin)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pizza_name', 'pizza_descript', 'pizza_weight', 'price')   # страница Pizza
    list_filter = ('price',)                                                   # фильтр на странице Pizza
    fieldsets = (                                                              # страница add Pizza
        (None, {
            'fields': ('pizza_name', )
        }),
        ('Описание', {
            'fields': ('pizza_descript',)
        }),
        (None, {
            'fields': ('pizza_weight', 'price')
        }),
    )

admin.site.register(Pizza, PizzaAdmin)