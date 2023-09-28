# Generated by Django 4.1.11 on 2023-09-28 05:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User_api', '0003_alter_userdata_demo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='demo',
        ),
        migrations.AddField(
            model_name='userdata',
            name='UserId',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='userdata',
            name='UserName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(default='', max_length=15),
        ),
    ]
