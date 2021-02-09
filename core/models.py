from django.db import models


class Order(models.Model):
    fullname = models.CharField(
        "Imię i nazwisko",
        max_length=50
        )
    address_1 = models.CharField(
        "Ulica oraz numer domu/mieszkania",
        max_length=350,
    )
    address_2 = models.CharField(
        "Miejscowość",
        max_length=350,
    )
    post_code = models.CharField(
        "Kod pocztowy",
        max_length=6,
    )
    email = models.EmailField(
        "Adres e-mail",
        max_length=254,
        )
    quantity = models.PositiveIntegerField(
        "Ilość"
    )

    def __str__(self):
        return f"{self.fullname} | {str(self.email)}"