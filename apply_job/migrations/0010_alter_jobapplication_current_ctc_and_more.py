# Generated by Django 4.1.2 on 2022-10-19 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apply_job", "0009_alter_jobapplication_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="current_ctc",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="jobapplication",
            name="position_applying",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="apply_job.position"
            ),
        ),
    ]
