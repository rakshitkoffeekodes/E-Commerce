# Generated by Django 4.2.2 on 2023-12-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile_no',
            field=models.CharField(default=0, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='media/'),
        ),
    ]
