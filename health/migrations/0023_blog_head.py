# Generated by Django 4.0.1 on 2022-02-18 18:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0022_rename_text_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='head',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
