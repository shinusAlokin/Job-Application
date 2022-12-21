# Generated by Django 4.1.2 on 2022-10-12 11:48

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('apply_job', '0002_rename_dob_jobapplication_date_of_birty_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='date_of_birty',
            new_name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]