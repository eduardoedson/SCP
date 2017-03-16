from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django_filters import FilterSet
from easy_select2 import Select2

from crispy_layout_mixin import form_actions, to_row
from utils import (TIPO_TELEFONE, YES_NO_CHOICES, get_medicos,
                   get_or_create_grupo)

from .models import Especialidade, EspecialidadeMedico, Usuario


class EspecialidadeMedicoFilterSet(FilterSet):

    class Meta:
        model = EspecialidadeMedico
        fields = ['especialidade']

    def __init__(self, *args, **kwargs):
        super(EspecialidadeMedicoFilterSet, self).__init__(*args, **kwargs)

        row1 = to_row([('especialidade', 12)])

        self.form.helper = FormHelper()
        self.form.helper.form_method = 'GET'
        self.form.helper.layout = Layout(
            Fieldset(_('Pesquisar Médico'),
                     row1, form_actions(save_label='Filtrar'))
        )


class MudarSenhaForm(forms.Form):
    nova_senha = forms.CharField(
        label="Nova Senha", max_length=30,
        widget=forms.PasswordInput(
          attrs={'class': 'form-control form-control-lg',
                 'name': 'senha',
                 'placeholder': 'Nova Senha'}))

    confirmar_senha = forms.CharField(
        label="Confirmar Senha", max_length=30,
        widget=forms.PasswordInput(
          attrs={'class': 'form-control form-control-lg',
                 'name': 'confirmar_senha',
                 'placeholder': 'Confirmar Senha'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username", max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg',
                   'name': 'username',
                   'placeholder': 'Usuário'}))

    password = forms.CharField(
        label="Password", max_length=30,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'name': 'password',
                   'placeholder': 'Senha'}))


class UsuarioForm(ModelForm):

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
                  'numero', 'complemento', 'bairro', 'referencia',
                  'primeiro_telefone', 'segundo_telefone']

        widgets = {'email': forms.TextInput(
                               attrs={'style': 'text-transform:lowercase;'})}

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['primeiro_telefone'].widget.attrs['class'] = 'telefone'
        self.fields['segundo_telefone'].widget.attrs['class'] = 'telefone'

    def valida_igualdade(self, texto1, texto2, msg):
        if texto1 != texto2:
            raise ValidationError(msg)
        return True

    def clean(self):

        if ('password' not in self.cleaned_data or
                'password_confirm' not in self.cleaned_data):
            raise ValidationError(_('Favor informar senhas atuais ou novas'))

        msg = _('As senhas não conferem.')
        self.valida_igualdade(
            self.cleaned_data['password'],
            self.cleaned_data['password_confirm'],
            msg)

        try:
            validate_password(self.cleaned_data['password'])
        except ValidationError as error:
            raise ValidationError(error)

        return self.cleaned_data

    @transaction.atomic
    def save(self, commit=False):
        usuario = super(UsuarioForm, self).save(commit)

        # Cria User
        u = User.objects.create(username=usuario.username, email=usuario.email)
        u.set_password(self.cleaned_data['password'])
        u.is_active = True
        u.groups.add(get_or_create_grupo(self.cleaned_data['tipo'].descricao))

        u.save()
        usuario.user = u
        usuario.save()
        return usuario


class UsuarioEditForm(ModelForm):

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

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nome', 'data_nascimento', 'sexo',
                  'plano', 'tipo', 'cep', 'end', 'numero', 'complemento',
                  'bairro', 'referencia', 'primeiro_telefone',
                  'segundo_telefone']

        widgets = {'username': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'email': forms.TextInput(
                                 attrs={'style': 'text-transform:lowercase;'}),
                   }

    def __init__(self, *args, **kwargs):
        super(UsuarioEditForm, self).__init__(*args, **kwargs)
        self.fields['primeiro_telefone'].widget.attrs['class'] = 'telefone'
        self.fields['segundo_telefone'].widget.attrs['class'] = 'telefone'

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

    @transaction.atomic
    def save(self, commit=False):
        usuario = super(UsuarioEditForm, self).save(commit)

        # Primeiro telefone
        tel = usuario.primeiro_telefone

        tel.tipo = self.data['primeiro_tipo']
        tel.ddd = self.data['primeiro_ddd']
        tel.numero = self.data['primeiro_numero']
        tel.principal = self.data['primeiro_principal']
        tel.save()

        usuario.primeiro_telefone = tel

        # Segundo telefone
        tel = usuario.segundo_telefone

        if tel:
            tel.tipo = self.data['segundo_tipo']
            tel.ddd = self.data['segundo_ddd']
            tel.numero = self.data['segundo_numero']
            tel.principal = self.data['segundo_principal']
            tel.save()
            usuario.segundo_telefone = tel

        # User
        u = usuario.user
        u.email = usuario.email
        u.groups.remove(u.groups.first())
        u.groups.add(get_or_create_grupo(self.cleaned_data['tipo'].descricao))

        u.save()
        usuario.save()
        return usuario


class EspecialidadeMedicoForm(ModelForm):

    medico = forms.ModelChoiceField(
        queryset=get_medicos(),
        widget=Select2(select2attrs={'width': '535px'}))

    especialidade = forms.ModelChoiceField(
        queryset=Especialidade.objects.all(),
        widget=Select2(select2attrs={'width': '535px'}))

    class Meta:
        model = EspecialidadeMedico
        fields = ['especialidade', 'medico']
