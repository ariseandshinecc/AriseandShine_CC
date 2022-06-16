# Generated by Django 3.1.2 on 2022-01-08 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20201123_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job_description',
            options={'verbose_name': 'Job description'},
        ),
        migrations.AlterModelOptions(
            name='job_requirement',
            options={'verbose_name': 'Job requirement'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-start_date', 'end_date'], 'verbose_name': 'Projects/Program'},
        ),
    ]