# Generated by Django 2.0.7 on 2018-12-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20181213_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='uri',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='symptom',
            name='uri',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
