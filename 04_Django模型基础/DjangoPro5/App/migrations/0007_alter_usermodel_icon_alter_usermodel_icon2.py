# Generated by Django 4.2 on 2024-05-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_usermodel_user_type2_usermodel_utype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='icon2',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads'),
        ),
    ]
