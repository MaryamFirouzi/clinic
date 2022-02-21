# Generated by Django 4.0.1 on 2022-02-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_doctor_deccription_doctor_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='deccription',
            new_name='description',
        ),
        migrations.AddField(
            model_name='clinic',
            name='Address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='opening_days',
            field=models.CharField(choices=[(0, 'شنبه'), (1, 'یکشنبه'), (2, 'دوشنبه'), (3, 'سه شنبه'), (4, 'چهارشنبه'), (5, 'پنجشنبه'), (6, 'جمعه')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='opening_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='clinic',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='clinic',
        ),
        migrations.AddField(
            model_name='doctor',
            name='clinic',
            field=models.ManyToManyField(to='health.Clinic'),
        ),
    ]
