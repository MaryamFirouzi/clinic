# Generated by Django 4.0.1 on 2022-02-18 17:43

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0020_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='describtion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
