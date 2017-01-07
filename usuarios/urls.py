from django.conf.urls import include, url
from .views import TipoUsuarioCrud

app_name = 'usuarios'

urlpatterns = [
    url(r'^tipo_usuario/', include(TipoUsuarioCrud.get_urls())),
]
