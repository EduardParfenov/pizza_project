# Generated by Django 4.1.7 on 2023-03-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_pizza_dough_pizza_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='status',
        ),
        migrations.AddField(
            model_name='salesman',
            name='first_name',
            field=models.CharField(blank=True, help_text='Enter seller name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='filling',
            field=models.CharField(blank=True, choices=[('1', 'Nothing'), ('2', 'Olives'), ('3', 'Sausage'), ('4', 'Pineapple'), ('5', 'Cucumbers')], default='1', help_text='Choose filling', max_length=1),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sauce',
            field=models.CharField(blank=True, choices=[('1', 'Nothing'), ('2', 'Tomato sauce'), ('3', 'Spicy sauce'), ('4', 'Milk sauce'), ('5', 'Garlic sause')], default='1', help_text='Choose sauce', max_length=1),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='title',
            field=models.CharField(blank=True, choices=[('1', 'Pepperoni'), ('2', 'BBQ'), ('3', 'Seafood')], default='1', help_text='Choose pizza', max_length=1),
        ),
        migrations.AlterField(
            model_name='salesman',
            name='full_name',
            field=models.CharField(blank=True, help_text='Enter seller name', max_length=30, null=True),
        ),
    ]
