from django.forms import ModelForm
from user.models import UserProfile
from django.utils.translation import gettext_lazy as _

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','birth_date','profile_picture']
        labels = {
            'phone': _('Numero de telefono'),
            'birth_date': _('Fecha de nacimiento'),
            'profile_picture': _('Imagen de perfil'),
        }        