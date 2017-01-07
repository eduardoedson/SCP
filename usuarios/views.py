from django.shortcuts import render
from .models import TipoUsuario
from crud.base import Crud

TipoUsuarioCrud = Crud.build(TipoUsuario, '')
