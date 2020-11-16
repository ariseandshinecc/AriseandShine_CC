# Generated by Django 3.1.2 on 2020-11-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20201024_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donor_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='caption',
            field=models.CharField(help_text='Provide a caption text of not more than 256 characters', max_length=256, unique=True, verbose_name='picture caption'),
        ),
        migrations.AlterField(
            model_name='newsevent',
            name='headline',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]