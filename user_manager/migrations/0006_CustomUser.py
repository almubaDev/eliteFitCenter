# Generated by Django 4.2.7 on 2023-12-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0005_CustomUser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='communication_preference',
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
    ]
