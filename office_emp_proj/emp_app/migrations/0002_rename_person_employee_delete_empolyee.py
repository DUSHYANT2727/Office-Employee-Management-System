# Generated by Django 4.2.4 on 2023-08-15 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='person',
            new_name='Employee',
        ),
        migrations.DeleteModel(
            name='Empolyee',
        ),
    ]
