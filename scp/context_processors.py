from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

from usuarios.models import Usuario


def recupera_user(request):
    try:
        pk = request.user.pk
    except:
        return 0
    else:
        if pk:
            try:
                usuario = Usuario.objects.get(user_id=pk)
            except ObjectDoesNotExist:
                return 0
            else:
                return usuario.pk
        else:
            return -1


def recupera_usuario(user_pk):
    if user_pk == 0:
        context = {'user_pk': user_pk,
                   'nome': 'Admin',
                   'tipo': 'Administrador'}
    elif user_pk == -1:
        context = {'user_pk': user_pk,
                   'nome': '',
                   'tipo': 'Deslogado'}
    else:
        usuario = Usuario.objects.get(pk=user_pk)
        if usuario.tipo.descricao == 'Médico':
            context = {'user_pk': user_pk,
                       'nome': usuario.nome,
                       'tipo': 'Médico'}
        elif usuario.tipo.descricao == 'Paciente':
            context = {'user_pk': user_pk,
                       'nome': usuario.nome,
                       'tipo': 'Paciente'}
        elif usuario.tipo.descricao == 'Administrador':
            context = {'user_pk': user_pk,
                       'nome': usuario.nome,
                       'tipo': 'Administrador'}
        else:
            context = {'user_pk': user_pk,
                       'nome': usuario.nome,
                       'tipo': 'Outro'}
    return context


def usuario_context(request):
    return recupera_usuario(recupera_user(request))
