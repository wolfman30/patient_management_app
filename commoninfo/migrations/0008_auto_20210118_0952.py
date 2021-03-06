# Generated by Django 3.1.4 on 2021-01-18 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commoninfo', '0007_auto_20210118_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(help_text="Enter the patient's phone number", max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Phone number should have only numbers.')]),
        ),
    ]
