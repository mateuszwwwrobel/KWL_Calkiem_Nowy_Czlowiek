from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.contrib.messages import get_messages

from core.forms import OrderForm
from core.views import OrderConfirmView


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestHomeView(TestCase):

    def test_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestListenView(TestCase):

    def test_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('/listen/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:listen'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:listen'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listen.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestConcertView(TestCase):

    def test_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('/concerts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:concerts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:concerts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'concerts.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestOrderFormView(TestCase):

    def test_view_url_exists_at_desired_location(self) -> None:
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self) -> None:
        response = self.client.get(reverse('core:order'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('core:order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_form.html')


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class TestOrderConfirmView(TestCase):

    def setUp(self) -> None:
        fullname = 'Mike Smith'
        address_1 = 'Silent Street 23'
        address_2 = 'Springfield'
        postcode = '12-123'
        email = 'mike@springfield.com'
        quantity = 1

        self.valid_order = OrderForm(data={
            'fullname': fullname,
            'email': email,
            'address_1': address_1,
            'address_2': address_2,
            'post_code': postcode,
            'quantity': quantity,
        })

    def test_redirect_with_valid_data(self) -> None:
        client = Client(enforce_csrf_checks=False)
        data = self.valid_order.data
        response = client.post(reverse('core:order-complete'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func.__name__, OrderConfirmView.as_view().__name__)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Dzięki! Płyta została zamówiona! Na podany adres mailowy '
                                           'zostały wysłane szczegóły zamówienia.')

    def test_redirect_with_zero_quantity(self) -> None:
        client = Client(enforce_csrf_checks=False)
        self.valid_order.data['quantity'] = 0
        data = self.valid_order.data
        response = client.post(reverse('core:order-complete'), data=data)
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Nie możesz zamówić 0 płyt. Wpisz poprawną wartość.')

    def test_redirect_with_invalid_data(self) -> None:
        client = Client(enforce_csrf_checks=False)
        self.valid_order.data['email'] = 'dasdasd'
        data = self.valid_order.data
        response = client.post(reverse('core:order-complete'), data=data)
        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Błąd w formularzu. Spróbuj jeszcze raz.')
