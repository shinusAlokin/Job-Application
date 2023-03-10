# Generated by Django 4.1.2 on 2022-10-19 09:01

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("apply_job", "0014_alter_jobapplication_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="address",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="city",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="current_ctc",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="date_of_birth",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="email",
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="expected_ctc",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="experience",
            field=models.CharField(
                choices=[
                    ("0", "Select"),
                    ("1", "Fresher"),
                    ("2", "1-2 years"),
                    ("3", "3-5 years"),
                    ("4", "6-8 years"),
                    ("5", "8+ years"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("O", "Other")], max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="github_url",
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="linkedin_url",
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="nationality",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region="US"
            ),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="position_applying",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="apply_job.position"
            ),
        ),
    ]
