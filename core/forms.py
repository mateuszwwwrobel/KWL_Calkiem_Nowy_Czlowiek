from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'order_name',
            'order_email',
            'order_address_1',
            'order_address_2',
            'post_code',
            'order_email',
            'order_amount',
            )
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'order_email': forms.TextInput(attrs={'class': 'form-control'}),
            'order_address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'order_address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'}),
            'order_amount': forms.TextInput(attrs={'class': 'form-control'}),
        }