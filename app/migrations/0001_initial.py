# Generated by Django 5.0.1 on 2024-02-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('doctor_name', models.CharField(max_length=255)),
                ('appointmaent_date', models.DateField()),
                ('time_slot', models.TimeField()),
                ('problem', models.TextField(max_length=255)),
            ],
        ),
    ]
