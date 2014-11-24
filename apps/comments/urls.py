from django.conf.urls import include, url
from .views import CrearComment, MostrarComments

urlpatterns = [
    # Examples:
    # url(r'^$', 'primerProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^comentar/$', CrearComment.as_view(), name='crear_comentario'),
    url(r'^mostrar/$', MostrarComments.as_view(), name='mostrar_comentarios'),
]
