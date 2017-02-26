from django.db import models
from django.utils.translation import ugettext_lazy as _

from usuarios.models import Usuario

class Medicamento(models.Model):
    id_medicamento = models.CharField(max_length=10, blank=True, null=True)
    principio_ativo = models.TextField(verbose_name=_('Principio Ativo'))
    cnpj = models.CharField(max_length=18, verbose_name=_('CNPJ'))
    laboratorio = models.TextField(verbose_name=_('Laboratório'))
    codggrem = models.CharField(max_length=18, verbose_name=_('codggrem'))
    ean = models.CharField(max_length=18, verbose_name=_('ean'))
    nome = models.TextField(verbose_name=_('Nome'))
    apresentacao = models.TextField(verbose_name=_('Apresentação'))
    preco_fabricacao = models.CharField(max_length=10, verbose_name=_('Preço Fabricação'), blank=True, null=True)
    preco_comercial = models.CharField(max_length=10, verbose_name=_('Preço Comercial'), blank=True, null=True)
    restricao_hospitalar = models.CharField(max_length=10, verbose_name=_('Restrição Hospitalar'), blank=True, null=True)

    class Meta:
        verbose_name = _('Medicamento')
        verbose_name_plural = _('Medicamentos')

    def __str__(self):
        return self.nome

class Cid(models.Model):
    cid_id = models.CharField(max_length=10, verbose_name=_('Cid ID'), unique=True)
    descricao = models.TextField(verbose_name=_('Descrição'))

    class Meta:
        verbose_name = _('Cid')
        verbose_name_plural = _('Cids')

    def __str__(self):
        return '%s - %s' % (self.cid_id, self.descricao)

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
    descricao = models.TextField(verbose_name=('Descrição'))
    status = models.ForeignKey(StatusChamado, verbose_name=_('Status'))
    autor = models.ForeignKey(Usuario, verbose_name=_('Autor'), blank=True)

    class Meta:
        verbose_name = _('Tipo de Usuário')
        verbose_name_plural = _('Tipos de Usuários')

    def __str__(self):
        return '%s [%s]' % (self.titulo, self.status)
