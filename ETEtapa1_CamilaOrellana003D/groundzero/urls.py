from django.urls import path
from .views import home, crearProveedorNuevo, Ver,form_mod_proveedor, eliminar_proveedor
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',home, name='home'),
    path('crear_proveedor_nuevo', crearProveedorNuevo, name="crearProveedorNuevo"),
    path('ver', Ver, name="ver"),
    path('modificar_proveedor/<id>', form_mod_proveedor, name="modificar_proveedor"),
    path('eliminar_proveedor/<id>', eliminar_proveedor, name="eliminar_proveedor")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
