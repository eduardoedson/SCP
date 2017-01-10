from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils import RANGE_SEXO, TIPO_TELEFONE, YES_NO_CHOICES


class TipoUsuario(models.Model):
    descricao = models.CharField(
        max_length=30, verbose_name=('Descrição'), unique=True)

    class Meta:
        verbose_name = _('Tipo de Usuário')
        verbose_name_plural = _('Tipos de Usuários')

    def __str__(self):
        return self.descricao


class PlanoSaude(models.Model):
    descricao = models.CharField(
        max_length=30, verbose_name=('Descrição'), unique=True)

    class Meta:
        verbose_name = _('Plano de Saúde')
        verbose_name_plural = _('Planos de Saúde')

    def __str__(self):
        return self.descricao


class Telefone(models.Model):
    tipo = models.CharField(
        max_length=7,
        choices=TIPO_TELEFONE,
        verbose_name=_('Tipo Telefone'),)
    ddd = models.CharField(max_length=2, verbose_name=_('DDD'))
    numero = models.CharField(max_length=10, verbose_name=_('Número'))
    principal = models.CharField(
        max_length=10,
        verbose_name=_('Telefone Principal?'),
        choices=YES_NO_CHOICES)

    class Meta:
        verbose_name = _('Telefone')
        verbose_name_plural = _('Telefones')

    def __str__(self):
        return '(%s) %s' % (self.ddd, self.numero)


class Usuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name=_('Nome'))
    data_nascimento = models.DateField(
        blank=True, null=True, verbose_name=_('Data de Nascimento'))
    sexo = models.CharField(
        max_length=1, verbose_name=_('Sexo'), choices=RANGE_SEXO)
    data_cadastro = models.DateField(auto_now_add=True)
    tipo = models.ForeignKey(TipoUsuario, verbose_name=_('Tipo de Usuário'))
    plano = models.ForeignKey(
        PlanoSaude, verbose_name=_('Plano de Saúde'), blank=True)

    # Telefones
    primeiro_telefone = models.ForeignKey(
        Telefone, null=True, related_name='primeiro_telefone')
    segundo_telefone = models.ForeignKey(
        Telefone, null=True, related_name='segundo_telefone')

    # Dados para logar no sistema
    user = models.ForeignKey(User)
    email = email = models.EmailField(unique=True, verbose_name=_('Email'))
    username = models.CharField(
        verbose_name=_('Nome de Usuário'), unique=True, max_length=20)

    # Endereço
    cep = models.CharField(max_length=30, verbose_name=_('CEP'), blank=True)
    end = models.CharField(
        max_length=50, verbose_name=_('Endereço'), blank=True)
    numero = models.CharField(
        max_length=50, verbose_name=_('Número'), blank=True)
    complemento = models.CharField(
        max_length=50, verbose_name=_('Complemento'), blank=True)
    bairro = models.CharField(
        max_length=30, verbose_name=_('Bairro'), blank=True)
    referencia = models.CharField(
        max_length=30, verbose_name=_('Ponto de Referência'), blank=True)

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')
        ordering = ['nome', 'tipo']

    def __str__(self):
        return '%s - %s' % (self.nome, self.tipo.descricao)
