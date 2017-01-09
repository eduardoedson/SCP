from django.views.generic import DetailView

import crud.base
from crud.base import Crud

from .forms import UsuarioForm
from .models import PlanoSaude, TipoUsuario, Usuario

TipoUsuarioCrud = Crud.build(TipoUsuario, '')
PlanoSaudeCrud = Crud.build(PlanoSaude, '')


class UsuarioCrud(Crud):
    model = Usuario
    help_path = ''

    class BaseMixin(crud.base.CrudBaseMixin):
        list_field_names = [
            'username', 'nome', 'data_nascimento', 'plano']

    class CreateView(crud.base.CrudCreateView):
        form_class = UsuarioForm

    class UpdateView(crud.base.CrudUpdateView):
        form_class = UsuarioForm

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
        #
        # @property
        # def layout_key(self):
        #     return 'UsuarioEdit'

    class DetailView(crud.base.CrudDetailView):

        def get_context_data(self, **kwargs):
            context = super(DetailView, self).get_context_data(**kwargs)

            tel1 = context['object'].primeiro_telefone
            tel1 = [('Primeiro Telefone'),
                    ('[%s] - %s' % (tel1.ddd, tel1.numero))]

            tel2 = context['object'].segundo_telefone or ''
            if tel2:
                tel2 = [('Segundo Telefone'),
                        ('[%s] - %s' % (tel2.ddd, tel2.numero))]

            context['telefones'] = [tel1, tel2]
            return context

        @property
        def layout_key(self):
            return 'UsuarioDetail'
