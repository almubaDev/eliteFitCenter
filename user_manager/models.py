from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Permission, Group
from django.utils import timezone
from django.db import models
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El campo "email" es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=('The groups this user belongs to.'),
        related_name='custom_users_groups'  
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='custom_users_permissions'  
    )

    GENDER_CHOICE = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro')
    ]

    COMMUNICATION_PREFERENCE_CHOICE = [
        ('T','Teléfono'),
        ('W','Whatsapp'),
        ('E','Email')
    ]

    email = models.EmailField(
        unique=True,  
        verbose_name = 'Correo electrónico',
        help_text='Ingrese una dirección de correo electrónico válido, personal y único.'
        )
    full_name = models.CharField(
        max_length=50,  
        verbose_name = 'Nombre completo',
        help_text='Ingrese su nombre completo tal como aparece en su documento de identidad.'
        )
    identification_document = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Documento de identidad',
        help_text='Ingrese el número de su documento de identidad, sin puntos ni guiones.'
    )
    is_passport = models.BooleanField(
        default=False,
        verbose_name='Es pasaporte',
        help_text='Marque esta opción si su documento de identidad es un passaporte.'
    )
    age = models.IntegerField(
        default=18,
        blank=False,
        null=False,
        verbose_name='Edad',
        help_text='Debes ser mayor de edad para inscribirte, si tienes entre 14 y 17 años puedes inscribirte presencialmente en nuestras sedes con autorización parental.'
    )
    gender = models.CharField( 
        max_length=1,
        choices=GENDER_CHOICE,
        blank=True,
        null=True,
        verbose_name='Género',
        help_text='Utilizado para personalizar programas de entrenamiento específicos.'
    )
    phone_number = models.CharField(
        max_length=20,  
        verbose_name = 'Número de teléfono'
    )
    is_trainer = models.BooleanField(
        default=False,
        verbose_name='Es entrenador'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Usuario activo'
    )
    is_staff = models.BooleanField(
        default=False,  
        verbose_name='Es parte del equipo'
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha del registro'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.email
