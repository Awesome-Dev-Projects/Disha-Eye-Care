# Generated by Django 4.0.4 on 2022-05-10 08:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(max_length=50)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=200)),
                ('prescription_date', models.DateField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('consultation_fee', models.PositiveIntegerField()),
                ('medicine_charges', models.PositiveIntegerField()),
                ('lab_fee', models.PositiveIntegerField()),
                ('other_charges', models.PositiveIntegerField()),
                ('total_amount', models.PositiveIntegerField()),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice_date', models.DateField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='DailySlotBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor_time_slot', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctortimeslot')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='daily_slot_booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.dailyslotbooking'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='patient.patient'),
        ),
    ]
