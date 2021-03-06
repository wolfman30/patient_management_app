# Generated by Django 3.1.4 on 2021-01-15 10:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commoninfo', '0003_auto_20210115_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='first_Name',
            field=models.CharField(help_text="Enter the patient's first name: ", max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed in names.')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_Name',
            field=models.CharField(help_text="Enter the patient's last name: ", max_length=20, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only letters are allowed in names.')]),
        ),
    ]
