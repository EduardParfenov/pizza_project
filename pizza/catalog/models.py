from django.db import models
from django.urls import reverse
from datetime import date
import uuid


class Salesman(models.Model):
    full_name = models.CharField(max_length=30, help_text="Enter seller name", null=True, blank=True)
    first_name = models.CharField(max_length=30, help_text="Enter seller name", null=True, blank=True)
    last_name = models.CharField(max_length=30, help_text="Enter seller name", null=True, blank=True)
    second_name = models.CharField(max_length=30, help_text="Enter seller name", null=True, blank=True)
    time_open = models.DateField('Open', null=True, blank=True)
    time_close = models.DateField('Close', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.full_name, self.time_open, self.time_close)


class Order(models.Model):
    list_pizza = models.ForeignKey('Pizza', on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(max_length=10)
    time_order = models.DateField('Time order', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.list_pizza, self.count, self.time_order)


class Pizza(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    price = models.IntegerField(max_length=10)

    LOAN_STATUS = (
        ('1', 'Pepperoni'),
        ('2', 'BBQ'),
        ('3', 'Seafood'),
    )
    title = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='1', help_text='Choose pizza')

    LOAN_STATUS = (
        ('1', 'Nothing'),
        ('2', 'Tomato sauce'),
        ('3', 'Spicy sauce'),
        ('4', 'Milk sauce'),
        ('5', 'Garlic sause')
    )
    sauce = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='1', help_text='Choose sauce')

    LOAN_STATUS = (
        ('1', 'Nothing'),
        ('2', 'Olives'),
        ('3', 'Sausage'),
        ('4', 'Pineapple'),
        ('5', 'Cucumbers')
    )
    filling = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='1', help_text='Choose filling')

    def __str__(self):
        return self.price