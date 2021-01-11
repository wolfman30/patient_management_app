# Generated by Django 3.1.4 on 2021-01-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commoninfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['unique_ID', 'first_Name', 'last_Name', 'date_of_birth', 'reason_for_visit']},
        ),
        migrations.AddField(
            model_name='patient',
            name='reason_for_visit',
            field=models.TextField(default='null', help_text='Enter the reason for visit', max_length=300),
        ),
    ]
