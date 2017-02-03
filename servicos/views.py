from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django_filters.views import FilterView

import crud.base
from crud.base import Crud
from scp.settings import LOGIN_REDIRECT_URL
from usuarios.models import Usuario
from utils import make_pagination

from .forms import ChamadoForm, ConsultaFilterSet, ConsultaForm
from .models import Chamado, Consulta, StatusChamado


class ConsultaFilterView(GroupRequiredMixin,
                         LoginRequiredMixin, FilterView):
    model = Consulta
    filterset_class = ConsultaFilterSet
    paginate_by = 10

    raise_exception = True
    login_url = LOGIN_REDIRECT_URL
    group_required = ['Administrador', 'Médico', 'Paciente']

    def get_context_data(self, **kwargs):
        context = super(ConsultaFilterView,
                        self).get_context_data(**kwargs)

        qr = self.request.GET.copy()
        paginator = context['paginator']
        page_obj = context['page_obj']
        context['page_range'] = make_pagination(
            page_obj.number, paginator.num_pages)
        context['qr'] = qr
        return context


class StatusChamadoCrud(Crud):
    model = StatusChamado
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        raise_exception = True
        login_url = LOGIN_REDIRECT_URL
        group_required = ['Administrador']


class ChamadoCrud(Crud):
    model = Chamado
    help_path = ''

    class BaseMixin(GroupRequiredMixin,
                    LoginRequiredMixin, crud.base.CrudBaseMixin):
        list_field_names = ['titulo', 'status']

        raise_exception = True
        login_url = LOGIN_REDIRECT_URL
        group_required = ['Administrador', 'Médico']

    class CreateView(crud.base.CrudCreateView):
        form_class = ChamadoForm

        def get_initial(self):
            status = StatusChamado.objects.get(descricao='Aberto')
            self.initial['status'] = status

            user = User.objects.get(id=self.request.user.id)
            try:
                usuario = Usuario.objects.get(user_id=user.id)
            except ObjectDoesNotExist:
                pass
            else:
                tipo = usuario.tipo

                if tipo.descricao == 'Médico':
                    self.initial['autor'] = usuario

            return self.initial.copy()

    class UpdateView(crud.base.CrudUpdateView):
        form_class = ChamadoForm

    class ListView(crud.base.CrudListView):
        def get_queryset(self):
            qs = super().get_queryset()
            try:
                usuario = Usuario.objects.get(user_id=self.request.user.id)
            except ObjectDoesNotExist:
                return qs
            else:
                if usuario.tipo.descricao == 'Médico':
                    return qs.filter(autor=usuario)
                else:
                    return qs


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
