# Generated by Django 2.1.1 on 2018-09-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FlimsImage',
            new_name='Album',
        ),
    ]
