from django.conf.urls import include, url

from .views import (ChamadoCrud, ConsultaCrud, ConsultaFilterView,
                    StatusChamadoCrud)

app_name = 'servicos'

urlpatterns = [
    url(r'^consulta/', include(ConsultaCrud.get_urls())),
    url(r'^chamado/', include(ChamadoCrud.get_urls())),
    url(r'^chamado/status', include(StatusChamadoCrud.get_urls())),
    url(r'^consulta/pesquisar/$', ConsultaFilterView.as_view(),
        name='pesquisar_consulta'),
]
