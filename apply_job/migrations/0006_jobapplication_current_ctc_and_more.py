# Generated by Django 4.1.2 on 2022-10-15 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apply_job', '0005_jobapplication_date_applied_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='current_ctc',
            field=models.CharField(default=450000, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='expected_ctc',
            field=models.CharField(default=6000000, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience',
            field=models.CharField(choices=[('0', 'Select'), ('1', '6 months'), ('2', '1-3'), ('3', '4-7')], default='Select', max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='gender',
            field=models.CharField(choices=[('S', 'Select'), ('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='position_applying',
            field=models.ForeignKey(default='select', on_delete=django.db.models.deletion.CASCADE, to='apply_job.position'),
        ),
    ]
