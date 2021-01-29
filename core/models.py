from django.db import models


class Order(models.Model):
    order_name = models.CharField(
        "Imię i nazwisko",
        max_length=255
        )
    order_address_1 = models.CharField(
        "Ulica oraz numer domu/mieszkania",
        max_length=1024,
    )
    order_address_2 = models.CharField(
        "Miejscowość",
        max_length=1024,
    )
    zip_code = models.CharField(
        "Kod pocztowy",
        max_length=6,
    )
    order_email = models.EmailField(
        "Adres e-mail",
        max_length=254,
        )
    order_amount = models.PositiveIntegerField(
        "Ilość"
    )

    def __str__(self):
        return f"{self.order_name} | {str(self.order_email)}"