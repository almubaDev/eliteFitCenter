# Generated by Django 4.2.7 on 2023-12-19 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0004_remove_customuser_authorization_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='health_history',
        ),
    ]
