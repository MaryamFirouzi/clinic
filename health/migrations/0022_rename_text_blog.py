# Generated by Django 4.0.1 on 2022-02-18 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0021_text_describtion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='text',
            new_name='Blog',
        ),
    ]