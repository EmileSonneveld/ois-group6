from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

# What does this mean?
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField(default=0)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


def __str__(self):
    return self.user.username


post_save.connect(create_profile, sender=User)


class Symptom(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    uri = models.CharField(max_length=500)

    def __str__(self):
        return self.name_slug

class Disease(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    uri = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name_slug
