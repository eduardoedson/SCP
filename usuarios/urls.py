from django.conf.urls import include, url

from .views import (EspecialidadeCreateView, EspecialidadeCrud,
                    EspecialidadeListView, EspecialidadeUpdateView,
                    PlanoSaudeCrud, TipoUsuarioCrud, UsuarioCrud, mudar_senha)

app_name = 'usuarios'

urlpatterns = [
    url(r'^tipo_usuario/', include(TipoUsuarioCrud.get_urls())),
    url(r'^plano_saude/', include(PlanoSaudeCrud.get_urls())),
    url(r'^especialidade/', include(EspecialidadeCrud.get_urls())),
    url(r'^usuario/', include(UsuarioCrud.get_urls())),
    url(r'^mudar_senha/$', mudar_senha, name='mudar_senha'),
    url(r'^usuario/(?P<pk>[0-9]+)/especialidade/create$',
        EspecialidadeCreateView.as_view(),
        name='especialidade_create'),
    url(r'^usuario/(?P<pk>[0-9]+)/especialidade$',
        EspecialidadeListView.as_view(),
        name='especialidade_list'),
    url(r'^usuario/(?P<pk>[0-9]+)/especialidade/update$',
        EspecialidadeUpdateView.as_view(),
        name='especialidade_update'),
]
