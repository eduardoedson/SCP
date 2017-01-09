from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from crispy_layout_mixin import form_actions
from utils import TIPO_TELEFONE, YES_NO_CHOICES

from .models import Telefone, Usuario


class UsuarioForm(ModelForm):
    # Primeiro Telefone
    primeiro_tipo = forms.ChoiceField(
        widget=forms.Select(),
        choices=TIPO_TELEFONE,
        label=_('Tipo Telefone'))
    primeiro_ddd = forms.CharField(max_length=2, label=_('DDD'))
    primeiro_numero = forms.CharField(max_length=10, label=_('Número'))
    primeiro_principal = forms.TypedChoiceField(
        widget=forms.Select(),
        label=_('Telefone Principal?'),
        choices=YES_NO_CHOICES)

    # Primeiro Telefone
    segundo_tipo = forms.ChoiceField(
        required=False,
        widget=forms.Select(),
        choices=TIPO_TELEFONE,
        label=_('Tipo Telefone'))
    segundo_ddd = forms.CharField(required=False, max_length=2, label=_('DDD'))
    segundo_numero = forms.CharField(
        required=False, max_length=10, label=_('Número'))
    segundo_principal = forms.ChoiceField(
        required=False,
        widget=forms.Select(),
        label=_('Telefone Principal?'),
        choices=YES_NO_CHOICES)

    # Usuário
    password = forms.CharField(
        max_length=20,
        label=_('Senha'),
        widget=forms.PasswordInput())

    password_confirm = forms.CharField(
        max_length=20,
        label=_('Confirmar Senha'),
        widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nome', 'password', 'password_confirm',
                  'data_nascimento', 'sexo', 'plano', 'tipo', 'cep', 'end',
                  'numero', 'complemento', 'bairro', 'referencia']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['primeiro_numero'].widget.attrs['class'] = 'telefone'
        self.fields['primeiro_ddd'].widget.attrs['class'] = 'ddd'
        self.fields['segundo_numero'].widget.attrs['class'] = 'telefone'
        self.fields['segundo_ddd'].widget.attrs['class'] = 'ddd'
        self.fields['cep'].widget.attrs['class'] = 'cep'
        # self.fields['data_nascimento'].widget.attrs['class'] = 'datepicker'

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    def clean_primeiro_numero(self):
        cleaned_data = self.cleaned_data

        telefone = Telefone()
        telefone.tipo = self.data['primeiro_tipo']
        telefone.ddd = self.data['primeiro_ddd']
        telefone.numero = self.data['primeiro_numero']
        telefone.principal = self.data['primeiro_principal']

        cleaned_data['primeiro_telefone'] = telefone
        return cleaned_data

    def clean_segundo_numero(self):
        cleaned_data = self.cleaned_data

        telefone = Telefone()
        telefone.tipo = self.data['segundo_tipo']
        telefone.ddd = self.data['segundo_ddd']
        telefone.numero = self.data['segundo_numero']
        telefone.principal = self.data['segundo_principal']

        cleaned_data['segundo_telefone'] = telefone
        return cleaned_data

    def valida_email_existente(self):
        return Usuario.objects.filter(
            email=self.cleaned_data['email']).exists()

    def clean(self):

        if ('password' not in self.cleaned_data or
                'password_confirm' not in self.cleaned_data):
            raise ValidationError(_('Favor informar senhas atuais ou novas'))

        msg = _('As senhas não conferem.')
        self.valida_igualdade(
            self.cleaned_data['password'],
            self.cleaned_data['password_confirm'],
            msg)

        if ('email' not in self.cleaned_data or
                'email_confirm' not in self.cleaned_data):
            raise ValidationError(_('Favor informar endereços de email'))

        msg = _('Os emails não conferem.')
        self.valida_igualdade(
            self.cleaned_data['email'],
            self.cleaned_data['email_confirm'],
            msg)

        email_existente = self.valida_email_existente()

        if email_existente:
            msg = _('Esse email já foi cadastrado.')
            raise ValidationError(msg)

        try:
            validate_password(self.cleaned_data['password'])
        except ValidationError as error:
            raise ValidationError(error)

        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=False):
        usuario = super(UsuarioForm, self).save(commit)

        # Cria telefones
        tel = Telefone.objects.create(
            tipo=self.data['primeiro_tipo'],
            ddd=self.data['primeiro_ddd'],
            numero=self.data['primeiro_numero'],
            principal=self.data['primeiro_principal']
        )
        usuario.primeiro_telefone = tel

        tel = self.cleaned_data['segundo_telefone']
        if (tel.tipo and tel.ddd and tel.numero and tel.principal):
            tel = Telefone.objects.create(
                tipo=self.data['segundo_tipo'],
                ddd=self.data['segundo_ddd'],
                numero=self.data['segundo_numero'],
                principal=self.data['segundo_principal']
            )
            usuario.segundo_telefone = tel

        # Cria User
        u = User.objects.create(username=usuario.username, email=usuario.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True

        u.save()
        usuario.user = u
        usuario.save()
        return usuario
