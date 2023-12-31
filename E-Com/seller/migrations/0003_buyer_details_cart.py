# Generated by Django 4.2.2 on 2023-12-23 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_register_mobile_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=200)),
                ('second_address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=25)),
                ('postcode', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=124)),
                ('email', models.CharField(max_length=50)),
                ('order_id', models.CharField(max_length=20)),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('product_color', models.CharField(max_length=50, null=True)),
                ('product_size', models.CharField(max_length=50, null=True)),
                ('stetus', models.BooleanField(default=True)),
                ('total', models.IntegerField(default=0)),
                ('Details_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.details')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.buyer')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
        ),
    ]
