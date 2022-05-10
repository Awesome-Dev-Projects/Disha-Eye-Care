# Generated by Django 4.0.4 on 2022-05-10 07:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import patient.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('secret', models.CharField(default='', max_length=100)),
                ('otp', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('expires_at', models.DateTimeField(default=patient.models.get_expiry_time)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='patient.patient')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('middle_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('gender', models.CharField(default='Male', max_length=30)),
                ('blood_group', models.CharField(default='', max_length=30)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
