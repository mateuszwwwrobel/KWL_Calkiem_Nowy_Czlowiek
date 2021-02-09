from core.models import Order
from django.test import TestCase


class TestOrder(TestCase):

    def setUp(self) -> None:
        Order.objects.create(
            quantity=4,
        )

    def test_fullname_label(self) -> None:
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('fullname').verbose_name
        self.assertEqual(field_label, 'Imię i nazwisko')

    def test_fullname_max_length(self) -> None:
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('fullname').max_length
        self.assertEqual(max_length, 50)

    def test_address1_label(self) -> None:
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('address_1').verbose_name
        self.assertEqual(field_label, 'Ulica oraz numer domu/mieszkania')

    def test_address1_max_length(self) -> None:
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('address_1').max_length
        self.assertEqual(max_length, 350)

    def test_address2_label(self) -> None:
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('address_2').verbose_name
        self.assertEqual(field_label, 'Miejscowość')

    def test_address2_max_length(self) -> None:
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('address_2').max_length
        self.assertEqual(max_length, 350)

    def test_post_code_label(self) -> None:
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('post_code').verbose_name
        self.assertEqual(field_label, 'Kod pocztowy')

    def test_post_code_max_length(self) -> None:
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('post_code').max_length
        self.assertEqual(max_length, 6)

    def test_email_label(self) -> None:
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'Adres e-mail')

    def test_email_max_length(self) -> None:
        order = Order.objects.get(id=1)
        max_length = order._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_quantity_type(self) -> None:
        order = Order.objects.get(id=1)
        var_type = order.quantity
        self.assertIsInstance(var_type, int)

    def test_object_name_is_fullname_pipe_email(self) -> None:
        order = Order.objects.get(id=1)
        expected_object_name = f'{order.fullname} | {order.email}'
        self.assertEqual(expected_object_name, str(order))
