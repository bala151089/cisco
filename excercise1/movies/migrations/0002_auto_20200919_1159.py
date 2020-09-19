# Generated by Django 2.2.14 on 2020-09-19 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='hostname',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Enter the valid hostname .', regex='([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')]),
        ),
        migrations.AlterField(
            model_name='router',
            name='ipAddress',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Enter the valid ipAddress Address.', regex='((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')]),
        ),
        migrations.AlterField(
            model_name='router',
            name='macAddress',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Enter the valid Mac Address.', regex='((?!-)[A-Za-z0-9-]{1, 63}(?<!-)\\\\.)+[A-Za-z]{2, 6}$')]),
        ),
    ]
