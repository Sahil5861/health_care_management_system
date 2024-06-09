# Generated by Django 5.0.2 on 2024-03-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_healthchceck'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=2048)),
            ],
        ),
    ]