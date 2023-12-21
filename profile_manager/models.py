from django.db import models
from user_manager.models import CustomUser



class SocialNetwork(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE)


class Instructor(models.Model):
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE
    )
    especialidad = models.CharField(
        max_length=50, 
        blank=False, 
        null=False)
    years_experience = models.IntegerField(
        blank=False, 
        null=False)
    about_me = models.TextField()
    social_networks = ''


class Member(models.Model):
    COMMUNICATION_PREFERENCE_CHOICE = [
        ('T','Teléfono'),
        ('W','Whatsapp'),
        ('E','Email')
    ]
    
    health_history = models.TextField(
        blank=True, null=True, 
        verbose_name = 'Historial de salud',
        help_text='Indique si padece alguna enfermedad o patologia de salud que sea incompatible con el esfuerzo físico o la realización de ciertos ejercicios.'
    )
    communication_preference = models.CharField( 
        max_length=1,
        choices=COMMUNICATION_PREFERENCE_CHOICE,
        verbose_name = 'Preferencia de comunicación',
        help_text = 'Escoja el canal por el cual desea que nos comuniquemos con usted.'
    )
    birthdate = models.DateField(
        blank=True, 
        null=True, 
        verbose_name = 'Fecha de nacimiento',
        help_text='Seleccione la fecha de su nacimiento.'
    )

    class Meta:
        verbose_name = 'Perfil de Miembro'
        verbose_name_plural = 'Perfiles de Miembros'
    
    def __str__(self) -> str:
        return f'Perfil de {self.user.email}'