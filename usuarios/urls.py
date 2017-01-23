from django.conf.urls import include, url

from .views import PlanoSaudeCrud, TipoUsuarioCrud, UsuarioCrud, mudar_senha

app_name = 'usuarios'

urlpatterns = [
    url(r'^tipo_usuario/', include(TipoUsuarioCrud.get_urls())),
    url(r'^plano_saude/', include(PlanoSaudeCrud.get_urls())),
    url(r'^usuario/', include(UsuarioCrud.get_urls())),
    url(r'^mudar_senha/$', mudar_senha, name='mudar_senha'),
]
