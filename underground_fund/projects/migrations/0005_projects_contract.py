# Generated by Django 4.1.2 on 2022-12-01 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='contract',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
