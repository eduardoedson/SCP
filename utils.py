from datetime import date

from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

import usuarios

RANGE_MESES = [
    (1, _('Janeiro')),
    (2, _('Fevereiro')),
    (3, _('Março')),
    (4, _('Abril')),
    (5, _('Maio')),
    (6, _('Junho')),
    (7, _('Julho')),
    (8, _('Agosto')),
    (9, _('Setembro')),
    (10, _('Outubro')),
    (11, _('Novembro')),
    (12, _('Dezembro')),
]

RANGE_ANOS = [(year, year) for year in range(date.today().year, 1889, -1)]

RANGE_SEXO = [('F', _('Feminino')), ('M', _('Masculino')), ('O', _('Outro'))]

TIPO_TELEFONE = [('FIXO', 'FIXO'), ('CELULAR', 'CELULAR')]

YES_NO_CHOICES = [(None, _('----')), (False, _('Não')), (True, _('Sim'))]


def from_to(start, end):
    return list(range(start, end + 1))


def make_pagination(index, num_pages):
    PAGINATION_LENGTH = 10
    if num_pages <= PAGINATION_LENGTH:
        return from_to(1, num_pages)
    else:
        if index - 1 <= 5:
            tail = [num_pages - 1, num_pages]
            head = from_to(1, PAGINATION_LENGTH - 3)
        else:
            if index + 1 >= num_pages - 3:
                tail = from_to(index - 1, num_pages)
            else:
                tail = [index - 1, index, index + 1,
                        None, num_pages - 1, num_pages]
            head = from_to(1, PAGINATION_LENGTH - len(tail) - 1)
        return head + [None] + tail


def get_medicos():
    tipo = usuarios.models.TipoUsuario.objects.get(descricao='Médico')
    return usuarios.models.Usuario.objects.filter(tipo=tipo)


def get_pacientes():
    tipo = usuarios.models.TipoUsuario.objects.get(descricao='Paciente')
    return usuarios.models.Usuario.objects.filter(tipo=tipo)


def get_or_create_grupo(nome):
    g = Group.objects.get_or_create(name=nome)
    return g[0]


def valida_igualdade(texto1, texto2):
    if texto1 != texto2:
        return False
    return True


class RangeWidgetOverride(forms.MultiWidget):

    def __init__(self, attrs=None):
        widgets = (forms.DateInput(format='%d/%m/%Y',
                                   attrs={'class': 'dateinput',
                                          'placeholder': 'Inicial'}),
                   forms.DateInput(format='%d/%m/%Y',
                                   attrs={'class': 'dateinput',
                                          'placeholder': 'Final'}))
        super(RangeWidgetOverride, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]

    def format_output(self, rendered_widgets):
        html = '<div class="col-sm-6">%s</div><div class="col-sm-6">%s</div>'\
            % tuple(rendered_widgets)
        return '<div class="row">%s</div>' % html
