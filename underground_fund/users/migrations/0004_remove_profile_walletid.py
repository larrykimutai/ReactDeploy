# Generated by Django 4.1.2 on 2022-12-01 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_walletid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='walletID',
        ),
    ]
