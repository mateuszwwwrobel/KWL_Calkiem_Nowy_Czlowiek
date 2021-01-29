from django.urls import path
from .views import HomeView, ConcertView, ListenView, OrderFormView, OrderConfirmView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('concerts', ConcertView.as_view(), name='concerts'),
    path('listen', ListenView.as_view(), name='listen'),
    path('order', OrderFormView.as_view(), name='order'),
    path('order-complete', OrderConfirmView.as_view(), name='order-complete'),
]