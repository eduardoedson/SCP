from django.db import models
from django.utils.translation import ugettext_lazy as _

from usuarios.models import Usuario


class Consulta(models.Model):
    medico = models.ForeignKey(
        Usuario, verbose_name=_('Médico'), related_name='medico')
    paciente = models.ForeignKey(
        Usuario, verbose_name=_('Paciente'), related_name='paciente')
    descricao = models.TextField(verbose_name=_('Descrição'))
