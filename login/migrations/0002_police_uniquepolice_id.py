# Generated by Django 4.0.4 on 2022-05-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='uniquepolice_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]