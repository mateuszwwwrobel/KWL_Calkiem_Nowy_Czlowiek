from core.forms import OrderForm
from django.test import TestCase


class OrderFormTest(TestCase):

    def setUp(self) -> None:
        fullname = 'Mike Smith'
        address_1 = 'Silent Street 23'
        address_2 = 'Springfield'
        postcode = '12-123'
        email = 'mike@springfield.com'
        quantity = 1

        self.form = OrderForm(data={
            'fullname': fullname,
            'email': email,
            'address_1': address_1,
            'address_2': address_2,
            'post_code': postcode,
            'quantity': quantity,
        })

    def test_form_fields_labels(self) -> None:
        form = OrderForm()
        self.assertTrue(form.fields['fullname'].label is None or
                        form.fields['fullname'].label == 'Imię i nazwisko')
        self.assertTrue(form.fields['address_1'].label is None or
                        form.fields['address_1'].label == 'Ulica oraz numer domu/mieszkania')
        self.assertTrue(form.fields['address_2'].label is None or
                        form.fields['address_2'].label == 'Miejscowość')
        self.assertTrue(form.fields['post_code'].label is None or
                        form.fields['post_code'].label == 'Kod pocztowy')
        self.assertTrue(form.fields['email'].label is None or
                        form.fields['email'].label == 'Adres e-mail')
        self.assertTrue(form.fields['quantity'].label is None or
                        form.fields['quantity'].label == 'Ilość')

    def test_form_email_field(self) -> None:
        email = 'useruser.com'
        self.form.data['email'] = email
        self.assertFalse(self.form.is_valid())

    def test_form_quantity_field(self):
        quantity = 'six'
        self.form.data['quantity'] = quantity
        self.assertFalse(self.form.is_valid())



