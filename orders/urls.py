from django.urls import path
from orders.views import add_order_view


urlpatterns = [
    path('add_order/', add_order_view, name='add_order'),
]
