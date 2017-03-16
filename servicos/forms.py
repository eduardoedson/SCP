from datetime import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout
from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django_filters import DateFromToRangeFilter, FilterSet
from easy_select2 import Select2

from crispy_layout_mixin import form_actions, to_row
from utils import RangeWidgetOverride, get_medicos, get_pacientes

from .models import Chamado, Consulta


class ConsultaFilterSet(FilterSet):

    filter_overrides = {models.DateField: {
        'filter_class': DateFromToRangeFilter,
        'extra': lambda f: {
            'label': '%s (%s)' % (f.verbose_name, 'Inicial - Final'),
            'widget': RangeWidgetOverride}
    }}

    class Meta:
        model = Consulta
        fileds = ['data']

    def __init__(self, *args, **kwargs):
        super(ConsultaFilterSet, self).__init__(*args, **kwargs)

        row1 = to_row([('data', 12)])

        self.form.helper = FormHelper()
        self.form.helper.form_method = 'GET'
        self.form.helper.layout = Layout(
            Fieldset(_('Pesquisar Consulta'),
                     row1, form_actions(save_label='Filtrar'))
        )


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


class ChamadoForm(ModelForm):

    class Meta:
        model = Chamado
        fields = '__all__'
        widgets = {'autor': forms.HiddenInput()}
