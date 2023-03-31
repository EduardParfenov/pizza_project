from django.contrib import admin
from .models import Salesman, Pizza, Order

# admin.site.register(Salesman)
# admin.site.register(Pizza)
# admin.site.register(Order)


class SalesmanAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'time_open', 'time_close')   # страница Salesman
    fields = ['first_name', 'last_name', ('time_open', 'time_close')]       # страница add Salesman
    list_filter = ('time_open',)                                            # фильтр на странице Salesman

admin.site.register(Salesman, SalesmanAdmin)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('list_pizza', 'count', 'time_order')                    # страница Order
    fields = ['list_pizza', ('count', 'time_order')]                        # страница add Order


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('pizza_name', 'pizza_descript', 'pizza_weight', 'price')   # страница Pizza
    list_filter = ('price',)                                                   # фильтр на странице Pizza
    fieldsets = (                                                              # страница add Pizza с разделами
        (None, {
            'fields': ('pizza_name', )
        }),
        ('Описание', {
            'fields': ('pizza_descript', )
        }),
        (None, {
            'fields': ('pizza_weight', 'price')
        }),
    )
