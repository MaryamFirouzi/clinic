# Generated by Django 4.0.1 on 2022-01-31 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.clinics'),
        ),
    ]
