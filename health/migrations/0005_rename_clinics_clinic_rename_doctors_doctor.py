# Generated by Django 4.0.1 on 2022-01-31 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_rename_doctor_doctors_clinic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clinics',
            new_name='Clinic',
        ),
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
    ]
