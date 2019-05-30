from django.conf.urls import url,include
from apps.mascota.views import index,mascota_view

urlpatterns = [

    url('^$', index, name='index'),
    url('^nuevo$', mascota_view, name='mascota_crear')

]