# Generated by Django 4.1.11 on 2023-09-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_api', '0002_userdata_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='demo',
            field=models.CharField(default='123', max_length=10),
        ),
    ]
