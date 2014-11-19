from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'primerProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Seccion del admin.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #URL de la pagina de usuarios.
    url(r'^usuarios/' , include('apps.usuarios.urls')),

    #URL en la cual se tienen las imagenes guardadas.
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, } ),
]