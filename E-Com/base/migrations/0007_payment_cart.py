# Generated by Django 4.2.2 on 2023-12-26 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_buyercart_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.buyercart'),
        ),
    ]
