from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.CharField(max_length=500)


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    occupation = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.BigIntegerField()
    reason = models.CharField(max_length=1000)
