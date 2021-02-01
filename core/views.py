from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import OrderForm
from .models import Order
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.views.generic import TemplateView, FormView, View
import os


class HomeView(TemplateView):
    template_name = 'index.html'


class ListenView(TemplateView):
    template_name = 'listen.html'


class ConcertView(TemplateView):
    template_name = 'concerts.html'


class OrderFormView(FormView):
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = 'core:order-complete'


class OrderConfirmView(View):
    def post(self, request):
        amount_so_far = self.total_quantity()
        amount_ordered = int(self.request.POST['quantity'])
        if amount_so_far is not None:
            total_amount = amount_so_far + amount_ordered
        else:
            total_amount = amount_ordered

        if amount_so_far is not None and total_amount > 50:
            messages.info(request, 'Przykro mi, wszystkie płyty zostały wyprzedane lub chcesz zamówić więcej '
                                   'niż jest na stanie!')
            amount_left = 50 - amount_so_far
            context = {
                'amount_left': amount_left,
            }
            return render(request, 'order_failed.html', context)

        form = OrderForm(request.POST or None)
        if form.is_valid():
            order_name = request.POST.get('fullname')
            mail = [request.POST.get('email'), os.environ['EMAIL_HOST_USER'], ]

            combined_address = f"{request.POST.get('address_1')} {request.POST.get('address_2')}"

            mail_data = {
                'full_name': order_name,
                'address': combined_address,
                'postcode': request.POST.get('post_code'),
                'amount': request.POST.get('quantity'),
            }

            if int(request.POST.get('quantity')) == 0:
                messages.warning(request, 'Nie możesz zamówić 0 płyt. Wpisz poprawną wartość.')
                return redirect('core:order')

            # Email sender:
            subject = f'Całkiem Nowy Człowiek - {str(order_name).capitalize()}'
            html_message = render_to_string('email.html', mail_data)
            message = strip_tags(html_message)

            send_mail(
                subject,
                message,
                os.environ['EMAIL_HOST_USER'],
                mail,
                html_message=html_message,
            )

            context = {
                'user': order_name,
            }

            form.save()
            messages.success(request, 'Dzięki! Płyta została zamówiona! Na podany adres mailowy '
                                      'zostały wysłane szczegóły zamówienia.')

            return redirect('core:order')

        else:
            messages.warning(request, 'Błąd w formularzu. Spróbuj jeszcze raz.')
            return redirect('core:order')

    @staticmethod
    def total_quantity() -> int:
        quantity = Order.objects.all().aggregate(total_quantity=Sum('quantity'))

        total = quantity['total_quantity']
        return total
