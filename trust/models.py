from django.db import models
import uuid
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


class Regulardonation(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    occupation = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.BigIntegerField()
    type = models.CharField(max_length=100)
    amount = models.BigIntegerField(blank=True,null=True)
    checksum_id = models.CharField(max_length=100, default=0)


class Anonymousdonation(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    zipcode = models.BigIntegerField()
    type = models.CharField(max_length=100)
    amount = models.BigIntegerField(blank=True,null=True)
    checksum_id = models.CharField(max_length=100, default=0)
