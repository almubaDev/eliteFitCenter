from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.utils import timezone
from ..models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 
                  'full_name', 
                  'identification_document', 
                  'is_passport',
                  'gender', 
                  'age', 
                  'phone_number',
                  'password1', 
                  'password2')
        
        widgets = {
            # 'birthdate' : forms.DateInput( attrs={'type': 'date' , 'value': f'{timezone.now().date()}'}),
            'email' : forms.EmailInput( attrs={'type': 'email', 'placeholder':'Correo electronico'}),
            'age' : forms.NumberInput( attrs={'type':'number', 'min': '18', 'max': '99'})
        }




class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 
                  'password')

class CustomChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = "La contraseña no puede parecerse a la anterior, ni ser totalmente numérica, ni tener menos de 8 caracteres."
    class Meta:
        model: CustomUser
        fields = ('password1', 
                  'password2')
        
class CustomResetPasswordForm(PasswordResetForm):
    class Meta:
        model: CustomUser
        fields = ('email',)