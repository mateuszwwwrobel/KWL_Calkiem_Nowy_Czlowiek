from django.shortcuts import render
from .models import Order
from .forms import OrderForm

# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def listen_view(request):
    return render(request, 'listen.html')


def concert_view(request):
    return render(request, 'concerts.html')


def order_form_view(request):
    form = OrderForm(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'order_form.html', context)

