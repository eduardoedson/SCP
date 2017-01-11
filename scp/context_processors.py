from django.core.exceptions import ObjectDoesNotExist
from usuarios.models import Usuario


def recupera_usuario(request):
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


def usuario_context(request):
    context = {'usuario_pk': recupera_usuario(request)}
    return context
