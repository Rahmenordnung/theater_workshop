# Generated by Django 2.2.4 on 2019-08-11 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater_operas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Opera',
            new_name='Work',
        ),
        migrations.RenameField(
            model_name='part',
            old_name='opera',
            new_name='work',
        ),
    ]
