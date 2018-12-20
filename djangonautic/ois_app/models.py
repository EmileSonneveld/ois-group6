from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# Always define an explicit primary key, just to be sure.
# Don't provide 'user friendly' names. Because they are not programmer friendly.

ADMIN_DOCTOR_ID = 1


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    speciality = models.CharField(max_length=1000)

    def __str__(self):
        return "<Doctor: " + self.user.__str__() + ">"


@receiver(models.signals.post_save, sender=DoctorProfile)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.user.is_staff = True
        instance.user.save()


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    date_of_birth = models.DateTimeField() # DateField is not suported in OWL
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "<Patient: " + self.user.__str__() + ">"


class Diagnosis(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, )
    symptom = models.ForeignKey('Symptom', on_delete=models.CASCADE, )

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    severity = models.IntegerField(default=0)  # [0,10]

    def __str__(self):
        return "<" + self.patient.__str__() + " has been diagnosed with " + self.symptom.__str__() + ">"


class Symptom(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    uri = models.CharField(max_length=500, null=True, blank=True)

    parent = models.ForeignKey('Symptom', on_delete=models.CASCADE, null=True, blank=True, related_name="contains")
    can_cause_symptom = models.ManyToManyField('Symptom', blank=True)
    can_cause_disease = models.ManyToManyField('Disease', blank=True)
    added_by = models.ForeignKey(DoctorProfile, default=ADMIN_DOCTOR_ID, on_delete=models.CASCADE)

    def __str__(self):
        stri = "<" + self.name_slug.__str__()
        if self.uri:
            stri += " : " + self.uri.__str__()
        stri += ">"
        return stri


class Disease(models.Model):
    name_slug = models.CharField(max_length=500, primary_key=True)
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    uri = models.CharField(max_length=500, null=True, blank=True)
    added_by = models.ForeignKey(DoctorProfile, default=ADMIN_DOCTOR_ID, on_delete=models.CASCADE)

    def __str__(self):
        return "<" + self.name_slug.__str__() + ">"


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()  # primary_key=True
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    related_disease = models.ManyToManyField(Disease, blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
