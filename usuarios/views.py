from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView

import crud.base
from crud.base import Crud
from scp.settings import LOGIN_REDIRECT_URL
from utils import valida_igualdade

from .forms import MudarSenhaForm, UsuarioEditForm, UsuarioForm
from .models import PlanoSaude, TipoUsuario, Usuario


def mudar_senha(request):

    if not request.user.is_authenticated():
        return render(request, '403.html', {})

    if request.method == 'GET':
        context = {'form': MudarSenhaForm}
        return render(request, 'mudar_senha.html', context)

    elif request.method == 'POST':
        form = MudarSenhaForm(request.POST)
        if form.is_valid():
            if (not valida_igualdade(form.cleaned_data['nova_senha'],
                                     form.cleaned_data['confirmar_senha'])):
                context = {'form': MudarSenhaForm,
                           'msg': 'As senhas não conferem.'}
                return render(request, 'mudar_senha.html', context)
            else:
                user = User.objects.get(id=request.user.id)
                user.set_password(form.cleaned_data['nova_senha'])
                user.save()
            return render(request, 'index.html', {'msg': 'Senha alterada.'})
        else:
            context = {'form': MudarSenhaForm,
                       'msg': 'Formulário inválido.'}
            return render(request, 'mudar_senha.html', context)


class PlanoSaudeCrud(Crud):
    model = PlanoSaude
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin,
                    crud.base.CrudBaseMixin):

        list_field_names = ['descricao']
        login_url = LOGIN_REDIRECT_URL
        raise_exception = True
        group_required = 'Administrador'


class TipoUsuarioCrud(Crud):
    model = TipoUsuario
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin,
                    crud.base.CrudBaseMixin):

        list_field_names = ['descricao']
        login_url = LOGIN_REDIRECT_URL
        raise_exception = True
        group_required = 'Administrador'


class UsuarioCrud(Crud):
    model = Usuario
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin,
                    crud.base.CrudBaseMixin):

        list_field_names = ['nome', 'data_nascimento', 'tipo']
        login_url = LOGIN_REDIRECT_URL
        raise_exception = True
        group_required = 'Administrador'

    class CreateView(crud.base.CrudCreateView):
        form_class = UsuarioForm

    class UpdateView(crud.base.CrudUpdateView):
        form_class = UsuarioEditForm

        def get_initial(self):
            if self.get_object():

                tel1 = self.get_object().primeiro_telefone
                self.initial['primeiro_tipo'] = tel1.tipo
                self.initial['primeiro_ddd'] = tel1.ddd
                self.initial['primeiro_numero'] = tel1.numero
                self.initial['primeiro_principal'] = tel1.principal

                tel2 = self.get_object().segundo_telefone
                if tel2:
                    self.initial['segundo_tipo'] = tel2.tipo
                    self.initial['segundo_ddd'] = tel2.ddd
                    self.initial['segundo_numero'] = tel2.numero
                    self.initial['segundo_principal'] = tel2.principal

            return self.initial.copy()

        @property
        def layout_key(self):
            return 'UsuarioEdit'

    class DetailView(crud.base.CrudDetailView):

        def get_context_data(self, **kwargs):
            context = super(DetailView, self).get_context_data(**kwargs)

            tel1 = context['object'].primeiro_telefone
            tel1 = '[%s] - %s' % (tel1.ddd, tel1.numero)

            tel2 = context['object'].segundo_telefone
            if tel2:
                tel2 = '[%s] - %s' % (tel2.ddd, tel2.numero)
            else:
                tel2 = '----'

            context['telefones'] = [tel1, tel2]
            return context

        @property
        def layout_key(self):
            return 'UsuarioDetail'
