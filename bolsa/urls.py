from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       
    url(r'^$', 'bolsa.views.inicio', name='inicio'),
    url(r'^login/$', 'bolsa.views.iniciar_sesion', name='login'),
    url(r'^registro/$', 'bolsa.views.Registro', name='registro'),
    url(r'^logout/$', 'bolsa.views.cerrar_sesion', name='logout'),
    url(r'^recuperar_contrasena/$', 'bolsa.views.Recuperar_contrasena', name='RecuperarContrasena'),
    url(r'^cambiar_pass/$', 'bolsa.views.Cambiar_pass', name='CambiarPassword'),

    url(r'^principal/$', 'Appi.views.Principal', name='principal'),
    url(r'^listar_solicitudes/$', 'Appi.views.Listar_solicitudes', name='ListarSolicitudes'),
    url(r'^cambiar_estado_usuario/$', 'Appi.views.Cambiar_estado_usuario', name='CambiarEstadoUsuario'),

        
    

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
