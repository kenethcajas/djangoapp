from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth.views import login

#para llamar a nuestra página para insertar tenemos que invocar la dirección /pelicula/nueva

# se puede crear un hipervinculo para llamarla, en este ejemplo hay que invocar manualmente la dirección.

urlpatterns = [

	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
    }),

   
    url(r'^$', views.vehiculo_lista),
    #url(r'^$', views.inicio),
    url(r'^vehiculo/(?P<pk>[0-9]+)/$', views.vehiculo_detalle),
    url(r'^vehiculo/nuevo/$', views.vehiculo_nuevo, name='vehiculo_nuevo'),
    url(r'^vehiculo/(?P<pk>[0-9]+)/edit/$', views.vehiculo_editar, name='vehiculo_editar'),
    url(r'^vehiculo/(?P<pk>\d+)/remove/$', views.vehiculo_eliminar, name='vehiculo_eliminar'),
    url(r'^marca/$', views.marca_lista, name='marca_lista'),
    url(r'^marca/(?P<pk>[0-9]+)/$', views.marca_detalle),
    url(r'^marca/nueva/$', views.marca_nueva, name='marca_nueva'),
    url(r'^marca/(?P<pk>[0-9]+)/edit/$', views.marca_editar, name='marca_editar'),
    url(r'^marca/(?P<pk>\d+)/remove/$', views.marca_eliminar, name='marca_eliminar'),
    url(r'^modelo/$', views.modelo_lista, name='modelo_lista'),
    url(r'^modelo/(?P<pk>[0-9]+)/$', views.modelo_detalle),
    url(r'^modelo/nuevo/$', views.modelo_nuevo, name='modelo_nuevo'),
    url(r'^modelo/(?P<pk>[0-9]+)/edit/$', views.modelo_editar, name='modelo_editar'),
    url(r'^modelo/(?P<pk>\d+)/remove/$', views.modelo_eliminar, name='modelo_eliminar'),





    ]

   