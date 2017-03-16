from django.conf.urls import include, url

from .views import (ChamadoCrud, CidCrud, ConsultaCrud, ConsultaFilterView,
                    ConsultaPrintView, MedicamentoCrud, StatusChamadoCrud)

app_name = 'servicos'

urlpatterns = [
    url(r'^consulta/', include(ConsultaCrud.get_urls())),
    url(r'^cid/', include(CidCrud.get_urls())),
    url(r'^medicamento/', include(MedicamentoCrud.get_urls())),
    url(r'^chamado/', include(ChamadoCrud.get_urls())),
    url(r'^chamado/status', include(StatusChamadoCrud.get_urls())),
    url(r'^consulta/pesquisar/$', ConsultaFilterView.as_view(),
        name='pesquisar_consulta'),
    url(r'^consulta/(?P<pk>\d+)/imprimir$',
        ConsultaPrintView.as_view(), name='consulta_print'),
]
