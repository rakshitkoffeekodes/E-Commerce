# Generated by Django 4.2.2 on 2023-12-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_rename_product_items_product_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.CharField(max_length=50, null=True),
        ),
    ]