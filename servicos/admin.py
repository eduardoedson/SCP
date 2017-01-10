from django.contrib import admin
from easy_select2 import select2_modelform
from .models import Consulta

ConsultaForm = select2_modelform(Consulta, attrs={'width': '250px'})


class ServicosAdmin(admin.ModelAdmin):
    form = ConsultaForm
