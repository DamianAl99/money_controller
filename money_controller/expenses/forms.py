from django.forms import ModelForm
from .models import Payout
from django.utils.translation import gettext_lazy as _

class PayoutForm(ModelForm):
    class Meta:
        model = Payout
        fields = ['pay_title', 'price']
        labels = {
            'pay_title': _('Nombre del Pago a Realizar'),
            'price': _('Precio'),
        }