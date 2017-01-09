from django.shortcuts import render
from .models import TipoUsuario, PlanoSaude
from crud.base import Crud

TipoUsuarioCrud = Crud.build(TipoUsuario, '')
PlanoSaudeCrud = Crud.build(PlanoSaude, '')
