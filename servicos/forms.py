from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from usuarios.models import Usuario
from .models import Consulta
from utils import get_medicos, get_pacientes
from easy_select2 import Select2
from datetime import datetime


class ConsultaForm(ModelForm):

    medico = forms.ModelChoiceField(
        queryset=get_medicos(),
        widget=Select2(select2attrs={'width': '535px'}))
    paciente = forms.ModelChoiceField(
        queryset=get_pacientes(),
        widget=Select2(select2attrs={'width': '535px'}))

    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'descricao', 'data', 'hora']

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields['data'].initial = datetime.now()
        self.fields['hora'].initial = datetime.now().strftime("%H:%M")
