# Generated by Django 4.0.1 on 2022-02-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0026_alter_comment_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='e_mail',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
