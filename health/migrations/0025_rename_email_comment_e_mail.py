# Generated by Django 4.0.1 on 2022-02-19 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0024_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='email',
            new_name='e_mail',
        ),
    ]