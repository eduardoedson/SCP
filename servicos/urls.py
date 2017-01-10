from django.conf.urls import include, url

from .views import ConsultaCrud

app_name = 'servicos'

urlpatterns = [
    url(r'^consulta/', include(ConsultaCrud.get_urls())),
]
