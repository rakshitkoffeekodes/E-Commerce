# Generated by Django 4.2.2 on 2023-12-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_register_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='profile_picture',
            field=models.FileField(default='default.jpg', upload_to='media/'),
        ),
    ]
