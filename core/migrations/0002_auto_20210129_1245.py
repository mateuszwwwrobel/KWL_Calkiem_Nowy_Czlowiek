# Generated by Django 3.0.8 on 2021-01-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_address_1',
            field=models.CharField(max_length=1024, verbose_name='Ulica oraz numer domu/mieszkania'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_address_2',
            field=models.CharField(max_length=1024, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_amount',
            field=models.PositiveIntegerField(verbose_name='Ilość'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_email',
            field=models.EmailField(max_length=254, verbose_name='Adres e-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_name',
            field=models.CharField(max_length=255, verbose_name='Imię i nazwisko'),
        ),
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.CharField(max_length=6, verbose_name='Kod pocztowy'),
        ),
    ]
