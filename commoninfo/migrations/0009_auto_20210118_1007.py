# Generated by Django 3.1.4 on 2021-01-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commoninfo', '0008_auto_20210118_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(help_text="Enter the patient's date of birth in the form of year-month-day"),
        ),
    ]
