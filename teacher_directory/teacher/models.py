from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import CharField


# Create your models here.
class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    profile_picture=models.ImageField(upload_to='uploads/',default='uploads/default.jpg',blank=True)
    email_address=models.EmailField(max_length=20,unique=True)
    phone_number=models.CharField(max_length=20)
    room_number=models.CharField(max_length=5)
    subjects_taught=models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    