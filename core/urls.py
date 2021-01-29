from django.contrib import admin
from django.urls import path
from .views import home_view, concert_view, listen_view, order_form_view, order_complete

app_name = 'core'

urlpatterns = [
    path('', home_view, name="home"),
    path('concerts', concert_view, name='concerts'),
    path('listen', listen_view, name='listen'),
    path('order', order_form_view, name='order'),
    path('order-complete', order_complete, name='order-complete'),
]