# Generated by Django 4.0.4 on 2022-05-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_criminalupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='missing',
            name='foundby',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='missing',
            name='foundpicture',
            field=models.ImageField(default='', upload_to='login/missing_found/images'),
        ),
    ]