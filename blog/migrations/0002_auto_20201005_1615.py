# Generated by Django 2.2.3 on 2020-10-05 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='createdtime',
            new_name='created_time',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='modifiedtime',
            new_name='modified_time',
        ),
    ]
