# Generated by Django 2.1.4 on 2018-12-21 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ois_app', '0002_auto_20181220_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
