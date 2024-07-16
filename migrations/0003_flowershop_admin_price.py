# Generated by Django 3.2.23 on 2024-01-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerbloom', '0002_flowershop'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowershop',
            name='admin_price',
            field=models.DecimalField(decimal_places=2, default=277, max_digits=10, verbose_name='Flower Price'),
            preserve_default=False,
        ),
    ]
