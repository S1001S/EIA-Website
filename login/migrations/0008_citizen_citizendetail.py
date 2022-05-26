# Generated by Django 4.0.4 on 2022-05-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_policeofficerdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('citizen_id', models.AutoField(primary_key=True, serialize=False)),
                ('citizenfirstname', models.CharField(max_length=100)),
                ('citizenlastname', models.CharField(max_length=100)),
                ('aadhar', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CitizenDetail',
            fields=[
                ('citizen_id', models.AutoField(primary_key=True, serialize=False)),
                ('citizenfirstname', models.CharField(max_length=100)),
                ('citizenlastname', models.CharField(max_length=100)),
                ('aadhar', models.CharField(default='', max_length=100)),
                ('citizenemail', models.CharField(default='', max_length=100)),
                ('citizenpassword', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
