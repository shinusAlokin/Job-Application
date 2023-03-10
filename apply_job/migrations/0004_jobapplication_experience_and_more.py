# Generated by Django 4.1.2 on 2022-10-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply_job', '0003_rename_date_of_birty_jobapplication_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='experience',
            field=models.CharField(choices=[('1', '0-2'), ('2', '2-5'), ('3', '5-8')], default='0-2', max_length=2),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('M', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='position_applying',
            field=models.ForeignKey(default='Software Engineer', on_delete=django.db.models.deletion.CASCADE, to='apply_job.position'),
        ),
    ]
