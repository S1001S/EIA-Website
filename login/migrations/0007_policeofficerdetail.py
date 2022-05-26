# Generated by Django 4.0.4 on 2022-05-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_policeofficer_uniquepolice_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceOfficerDetail',
            fields=[
                ('police_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('uniquepoliceid', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
