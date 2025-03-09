from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from orders.views import *

urlpatterns = [
    path('order/details',order_details,name="orders"),
    
]

