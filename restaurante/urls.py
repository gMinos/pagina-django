from django.contrib import admin
from django.urls import path
from miapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="principal"),
    path('registrarse/', views.registrarse, name="registrarse"),
    path('iniciar_sesion/', views.iniciar_session, name="iniciar_sesion"),
    path('cerra_sesion/', views.cerrar_session, name="cerrar_sesion"),
    path('contacto/', views.contacto, name="contacto"),
    path('informacion/', views.informacion_plato, name='informacion'),
    path('comidas_preferidas/', views.comidas_preferidas, name='preferencias'),
    path('editar_preferencia/<int:id_preferencia>/', views.editar_preferencia, name='editar_preferencia'),
    path('editar_preferencia/<int:id_preferencia>/actualizar', views.editar_preferencia, name='editar_preferencia'),
    path('editar_preferencia/<int:id_preferencia>/eliminar', views.eliminar_preferencia, name='eliminar_preferencia'),
    path('editar_preferencia/crear_preferencia', views.agregar_preferencia, name='agregar_preferencia'),
]
