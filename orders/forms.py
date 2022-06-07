from django import forms
from .models import Order
from localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField

class OrderCreateForm(forms.ModelForm):

    # postal_code = BRZipCodeField(label='CEP')
    # cpf = BRCPFField(label='CPF')
    # cnpj = BRCNPJField(label='CNPJ')


    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
