from django.db import models
from django.utils.translation import ugettext_lazy as _

from usuarios.models import Usuario


class Consulta(models.Model):
    medico = models.ForeignKey(
        Usuario, verbose_name=_('Médico'), related_name='medico')
    paciente = models.ForeignKey(
        Usuario, verbose_name=_('Paciente'), related_name='paciente')
    descricao = models.TextField(verbose_name=_('Descrição'))
    data = models.DateField(
        blank=True, null=True, verbose_name=_('Data da Consulta'))
    hora = models.CharField(
        blank=True, null=True,
        max_length=10, verbose_name=_('Hora da Consulta'))

    class Meta:
        verbose_name = _('Consulta')
        verbose_name_plural = _('Consultas')
        ordering = ['data', 'medico', 'paciente']

    def __str__(self):
        return '%s - %s | %s' % (self.nome, self.tipo.descricao, self.data)
