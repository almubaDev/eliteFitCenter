# Generated by Django 5.0 on 2023-12-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_alter_customuser_authorization_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birthdate',
            field=models.DateField(blank=True, help_text='Seleccione la fecha de su nacimiento.', null=True, verbose_name='Fecha de nacimiento'),
        ),
    ]
