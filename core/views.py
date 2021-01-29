from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
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

def order_complete(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        order_name = request.POST.get('order_name')
        mail = [request.POST.get('order_email'), ]
        
        #Email sender: 
        subject = f'Całkiem Nowy Człowiek -{str(order_name)}'
        message = f"Dziękuję za złożenie zamówienia {order_name}. Dokonaj płatności na podany niżej numer konta, a o resztę nic się nie martw!"

        send_mail(
            subject, 
            message, 
            'matthew.sparrow91@gmail.com', 
            mail, 
        )

        context = {
            'user': order_name,
        }

        form.save()

    return render(request, 'order-complete.html', context)