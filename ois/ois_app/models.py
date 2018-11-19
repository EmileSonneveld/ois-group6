from django.db import models

# Create your models here.

# Don't specify "human readable" names please. 
# We are computer scientists, not humans ;)


class Account(models.Model):
    email = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

class Doctor(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=1000)

class Patient(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_of_birth = models.DateTimeField()

class Symptom(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    uri = models.CharField(max_length=500)

class Disease(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    uri = models.CharField(max_length=500)
