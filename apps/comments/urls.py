from django.conf.urls import include, url
from .views import CrearComment, MostrarComments
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Examples:
    # url(r'^$', 'primerProyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^comentar/$', login_required(CrearComment.as_view()), name='crear_comentario'),
    url(r'^mostrar/$', MostrarComments.as_view(), name='mostrar_comentarios'),
]
