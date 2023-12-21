# Generated by Django 4.2.7 on 2023-12-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0008_CustomUser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(default=18, help_text='Debes ser mayor de edad para inscribirte, si tienes entre 14 y 17 años puedes inscribirte presencialmente en nuestras sedes con autorización parental.', verbose_name='Edad'),
        ),
    ]
