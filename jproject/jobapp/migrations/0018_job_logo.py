# Generated by Django 5.0.6 on 2024-06-29 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_userprofile_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='job_logos/'),
        ),
    ]
