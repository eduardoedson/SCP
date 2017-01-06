from datetime import date
from django.utils.translation import ugettext_lazy as _


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
