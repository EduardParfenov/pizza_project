from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('pizza/', views.PizzaListView.as_view(), name='pizza'),
    path(r'pizza/(?P<pk>\d+)', views.PizzaDetailView.as_view(), name='pizza-detail'),
    #path('pizza/<int:pk>', views.PizzaDetailView.as_view(), name='pizza-detail'),
]

urlpatterns += [
    path('order/', views.OrderListView.as_view(), name='order'),
]
