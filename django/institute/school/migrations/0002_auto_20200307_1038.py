# Generated by Django 3.0.4 on 2020-03-07 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
        migrations.AlterModelTable(
            name='student',
            table='student',
        ),
    ]
