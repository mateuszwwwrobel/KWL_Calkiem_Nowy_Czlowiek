from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'index.html')


def listen_view(request):
    return render(request, 'listen.html')


def concert_view(request):
    return render(request, 'concert.html')


def order_form_view(request):
    return render(request, 'order_form.html')