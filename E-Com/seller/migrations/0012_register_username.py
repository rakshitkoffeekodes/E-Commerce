# Generated by Django 4.2.2 on 2024-01-05 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_product_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
