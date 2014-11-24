from django.conf.urls import include, url
from .views import Registrarse

urlpatterns = [
    # Examples:
    # url(r'^$', 'primerProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$' , PaginaInicio.as_view() , name="inicio"),
    #URL's que utiliza el sistema de autenticacion de Django y usa el template inicio/inicio
    
    #URL de login
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'inicio/inicio.html'}, name="inicio"),
    
    #URL de logout
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name="logout"),

    #URL de registros
    url(r'^registrarse/$', Registrarse.as_view(), name="registrarse"),
]