# Generated by Django 4.2.7 on 2023-12-18 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0003_alter_customuser_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='authorization_file',
        ),
    ]
