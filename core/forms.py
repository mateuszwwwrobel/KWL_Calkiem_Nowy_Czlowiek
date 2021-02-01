from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'fullname',
            'email',
            'address_1',
            'address_2',
            'post_code',
            'email',
            'quantity',
            )
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_2': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
        }
