from django.shortcuts import render
from django.core.mail import send_mail
from .forms import OrderForm
from django.utils.html import strip_tags
from django.template.loader import render_to_string


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
        mail = [request.POST.get('order_email'), 'kwlrec@gmail.com']

        combined_address = f"{request.POST.get('order_address_1')} {request.POST.get('order_address_2')}"

        mail_data = {
            'full_name': order_name,
            'address': combined_address,
            'postcode': request.POST.get('post_code'),
            'amount': request.POST.get('order_amount'),
            }

        # Email sender:
        subject = f'Całkiem Nowy Człowiek - {str(order_name).capitalize()}'
        html_message = render_to_string('email.html', mail_data)
        message = strip_tags(html_message)

        send_mail(
            subject, 
            message, 
            'matthew.sparrow91@gmail.com', 
            mail,
            html_message=html_message,
        )

        context = {
            'user': order_name,
        }

        form.save()
    else:
        raise ValueError("Form is not valid.")

    return render(request, 'order-complete.html', context)