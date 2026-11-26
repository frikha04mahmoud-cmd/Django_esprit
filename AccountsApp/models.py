from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
class Doctor(User):
    license_number = models.CharField(max_length=6,unique=True)
    phone_number = models.CharField(max_length=8)
    specialities = models.ManyToManyField('Speciality',related_name='doctors',null=True,blank=True)
class Speciality(models.Model):
    name = models.CharField(max_length=100)
class Patient(User):
    id_national= models.CharField(max_length=8,unique=True)
    phone_number = models.CharField(max_length=8)
    birth_date = models.DateField()