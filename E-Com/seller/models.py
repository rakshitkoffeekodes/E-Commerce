from django.db import models


# Create your models here.

class Register(models.Model):
    profile_picture = models.FileField(upload_to="media/", default="default.jpg")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(unique=True, max_length=10, default=0)
    address = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name
