from django.conf.urls import include, url
from .views import RegistrarUsuario, MostrarUsuarios

urlpatterns = [
    # Examples:
    # url(r'^$', 'primerProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^alta/$' , RegistrarUsuario.as_view() , name="registrar_usuarios"),
    url(r'^mostrar/$' , MostrarUsuarios.as_view() , name="mostrar_usuarios"),
]
