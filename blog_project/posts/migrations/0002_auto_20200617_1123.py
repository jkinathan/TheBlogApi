# Generated by Django 2.2.13 on 2020-06-17 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_by',
            new_name='created_at',
        ),
    ]
