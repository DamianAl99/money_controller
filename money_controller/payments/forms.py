from django.forms import ModelForm
from .models import Groups_Pay
from django.utils.translation import gettext_lazy as _

class GroupsForm(ModelForm):
    class Meta:
        model = Groups_Pay
        fields = ['Title_groups', 'description', 'budget']
        labels = {
            'Title_groups': _('Titulo del Grupo'),
            'description': _('Descripcion'),
            'budget': _('Presupuesto Inicial'),
        }