# Generated by Django 4.0.1 on 2022-01-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_rename_clinics_clinic_rename_doctors_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='deccription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(null=True, upload_to='doctor'),
        ),
    ]
