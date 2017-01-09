from django.conf.urls import include, url

from .views import PlanoSaudeCrud, TipoUsuarioCrud, UsuarioCrud

app_name = 'usuarios'

urlpatterns = [
    url(r'^tipo_usuario/', include(TipoUsuarioCrud.get_urls())),
    url(r'^plano_saude/', include(PlanoSaudeCrud.get_urls())),
    url(r'^usuario/', include(UsuarioCrud.get_urls())),
]
