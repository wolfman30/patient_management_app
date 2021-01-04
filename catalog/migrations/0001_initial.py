# Generated by Django 3.1.4 on 2021-01-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('unique_ID', models.CharField(help_text="Enter the patient's unique ID: ", max_length=20, primary_key=True, serialize=False, unique=True)),
                ('first_Name', models.CharField(help_text="Enter the patient's first name: ", max_length=20)),
                ('last_Name', models.CharField(help_text="Enter the patient's last name: ", max_length=20)),
                ('date_of_birth', models.DateField(help_text="Enter the patient's date of birth: ")),
            ],
            options={
                'ordering': ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth'],
            },
        ),
    ]
