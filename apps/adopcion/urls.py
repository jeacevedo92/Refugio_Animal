from django.conf.urls import url
from apps.adopcion.views import index

urlpatterns=[
    url('', index),
    url('home', index),

]