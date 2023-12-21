# Generated by Django 4.2.3 on 2023-12-20 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50)),
                ('years_experience', models.IntegerField()),
                ('about_me', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_history', models.TextField(blank=True, help_text='Indique si padece alguna enfermedad o patologia de salud que sea incompatible con el esfuerzo físico o la realización de ciertos ejercicios.', null=True, verbose_name='Historial de salud')),
                ('communication_preference', models.CharField(choices=[('T', 'Teléfono'), ('W', 'Whatsapp'), ('E', 'Email')], help_text='Escoja el canal por el cual desea que nos comuniquemos con usted.', max_length=1, verbose_name='Preferencia de comunicación')),
                ('birthdate', models.DateField(blank=True, help_text='Seleccione la fecha de su nacimiento.', null=True, verbose_name='Fecha de nacimiento')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]