# Generated by Django 3.0.2 on 2020-03-04 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine_app', '0004_auto_20200303_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userportal',
            old_name='data',
            new_name='updatedate',
        ),
    ]