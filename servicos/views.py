from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

import crud.base
from crud.base import Crud
from scp.settings import LOGIN_REDIRECT_URL
from usuarios.models import Usuario

from .forms import ConsultaForm
from .models import Consulta


class ConsultaCrud(Crud):
    model = Consulta
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin,
                    crud.base.CrudBaseMixin):

        list_field_names = ['medico', 'paciente']
        login_url = LOGIN_REDIRECT_URL
        raise_exception = True
        group_required = ['Administrador', 'Médico', 'Paciente']

    class CreateView(crud.base.CrudCreateView):
        form_class = ConsultaForm

    class UpdateView(crud.base.CrudUpdateView):
        form_class = ConsultaForm

    class ListView(crud.base.CrudListView):
        def get_queryset(self):
            qs = super().get_queryset()
            try:
                usuario = Usuario.objects.get(user_id=self.request.user.id)
            except ObjectDoesNotExist:
                return qs
            else:
                if usuario.tipo.descricao == 'Médico':
                    return qs.filter(medico=usuario)
                elif usuario.tipo.descricao == 'Paciente':
                    return qs.filter(paciente=usuario)
                else:
                    return qs
