from django.core.exceptions import ObjectDoesNotExist
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
            return 0


def recupera_usuario(user_pk):
    if user_pk == 0:
        context = {'user_pk': 0,
                   'nome': 'Admin',
                   'tipo': 'Administrador'}
    else:
        usuario = Usuario.objects.get(pk=user_pk)
        if usuario.tipo.descricao == 'Médico':
            context = {'user_pk': user_pk,
                       'nome': usuario.nome,
                       'tipo': 'Médico'}
        elif usuario.tipo.descricao == 'Paciente':
            context = {'pk': user_pk,
                       'nome': usuario.npme,
                       'tipo': 'Paciente'}
        else:
            context = {'pk': user_pk,
                       'nome': usuario.npme,
                       'tipo': 'Outro'}
    return context


def usuario_context(request):
    return recupera_usuario(recupera_user(request))
