from django.conf.urls import include, url
from .views import RegistrarUsuario, MostrarUsuarios
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Examples:
    # url(r'^$', 'primerProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^alta/$' , RegistrarUsuario.as_view() , name="registrar_usuarios"),
    url(r'^mostrar/$' , login_required(MostrarUsuarios.as_view()) , name="mostrar_usuarios"),
]
