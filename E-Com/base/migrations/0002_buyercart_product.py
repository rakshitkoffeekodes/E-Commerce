# Generated by Django 4.2.2 on 2023-12-26 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_remove_cart_buyer_remove_cart_product_and_more'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyercart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.product'),
        ),
    ]
