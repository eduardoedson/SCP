from django.shortcuts import render

import crud.base
from crud.base import Crud

from .forms import ConsultaForm
from .models import Consulta


class ConsultaCrud(Crud):
    model = Consulta
    help_path = ''

    class BaseMixin(crud.base.CrudBaseMixin):
        list_field_names = ['medico', 'paciente']

    class CreateView(crud.base.CrudCreateView):
        form_class = ConsultaForm

    class UpdateView(crud.base.CrudUpdateView):
        form_class = ConsultaForm
