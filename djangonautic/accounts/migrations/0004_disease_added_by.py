# Generated by Django 2.0.7 on 2018-12-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181213_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.DoctorProfile'),
        ),
    ]
