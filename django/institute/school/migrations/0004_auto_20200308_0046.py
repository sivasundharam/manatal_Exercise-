# Generated by Django 3.0.4 on 2020-03-07 19:16

from django.db import migrations, models
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200308_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_identification',
            field=models.CharField(default=school.models.generateUUID, max_length=20, unique=True),
        ),
    ]
