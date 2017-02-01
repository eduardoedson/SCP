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
        return '-'


class StatusChamado(models.Model):
    descricao = models.CharField(
        max_length=30, verbose_name=('Descrição'), unique=True)

    class Meta:
        verbose_name = _('Tipo de Usuário')
        verbose_name_plural = _('Tipos de Usuários')

    def __str__(self):
        return self.descricao


class Chamado(models.Model):
    titulo = models.CharField(max_length=30, verbose_name=('Título'))
    descricao = models.CharField(max_length=30, verbose_name=('Descrição'))
    status = models.ForeignKey(StatusChamado, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Tipo de Usuário')
        verbose_name_plural = _('Tipos de Usuários')

    def __str__(self):
        return '%s [%s]' % (self.titulo, self.status)
