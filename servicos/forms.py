from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from usuarios.models import Usuario
from .models import Consulta
from utils import get_medicos, get_pacientes
from easy_select2 import Select2


class ConsultaForm(ModelForm):

    medico = forms.ModelChoiceField(queryset=get_medicos(), widget=Select2())
    paciente = forms.ModelChoiceField(
        queryset=get_pacientes(), widget=Select2())

    class Meta:
        model = Consulta
        fields = ['medico', 'paciente', 'descricao']