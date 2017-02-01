from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import crud.base
from crud.base import Crud
from usuarios.models import Usuario

from .forms import ConsultaForm
from .models import Consulta


class ConsultaCrud(Crud):
    model = Consulta
    help_path = ''

    class BaseMixin(crud.base.CrudBaseMixin):

        list_field_names = ['medico', 'paciente', 'data']

    class CreateView(crud.base.CrudCreateView):
        form_class = ConsultaForm

        def get_initial(self):
            user = User.objects.get(id=self.request.user.id)
            try:
                usuario = Usuario.objects.get(user_id=user.id)
            except ObjectDoesNotExist:
                pass
            else:
                tipo = usuario.tipo

                if tipo.descricao == 'Médico':
                    self.initial['medico'] = usuario

            return self.initial.copy()

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
