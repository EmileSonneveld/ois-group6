from django.db import models

# Create your models here.

# Don't specify "human readable" names please. 
# We are computer scientists, not humans ;)

# Dont use 'pk' (primary_key) as table name!

class Account(models.Model):
    email = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.email + " name: " + self.name

class Doctor(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=1000)
    def __str__(self):
        return self.account_id.__str__() + " speciality: " + self.speciality[0:5]

class Patient(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.account_id.__str__() + " date_of_birth: " + str(self.date_of_birth)


class Symptom(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    uri = models.CharField(max_length=500)

class Disease(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    uri = models.CharField(max_length=500)
