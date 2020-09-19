# Generated by Django 2.2.14 on 2020-09-19 11:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapid', models.CharField(max_length=100)),
                ('macAddress', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Enter the valid Mac Address.', regex='((?!-)[A-Za-z0-9-]{1, 63}(?<!-)\\\\.)+[A-Za-z]{2, 6}$')])),
                ('hostname', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Enter the valid hostname .', regex='([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')])),
                ('ipAddress', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Enter the valid ipAddress Address.', regex='((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'router',
            },
        ),
    ]
