# Generated by Django 3.1.4 on 2021-01-20 03:17

import commoninfo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commoninfo', '0009_auto_20210118_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(help_text="Enter the patient's date of birth in the form of year-month-day", validators=[commoninfo.models.validate_birthyear]),
        ),
    ]
