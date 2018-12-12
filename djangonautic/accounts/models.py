from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=1000)

    def __str__(self):
        return "<Doctor: " + self.user.__str__() + ">"


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "<Patient: " + self.user.__str__() + ">"


# def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#
# def __str__(self):
#    return self.user.username
#
# post_save.connect(create_profile, sender=User)


class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey('PatientProfile', on_delete=models.CASCADE, )
    symptom = models.ForeignKey('Symptom', on_delete=models.CASCADE, )

    start_date = models.DateField()
    end_date = models.DateField()
    severity = models.IntegerField(default=0)

    def __str__(self):
        return "<" + self.patient.__str__() + " has been diagnosed with " + self.symptom.__str__() + ">"


class Symptom(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    uri = models.CharField(max_length=500)

    def __str__(self):
        return "<" + self.name_slug.__str__() + ">"


class Disease(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    uri = models.CharField(max_length=500)

    def __str__(self):
        return "<" + self.name_slug.__str__() + ">"
