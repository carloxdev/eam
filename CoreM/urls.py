# -*- coding: utf-8 -*-

# Librerias django
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

# API Rest
from rest_framework import routers

# API Rest - Views:
from activos.views import EquipoAPI
from activos.views import UbicacionAPI
from activos.views import UbicacionAPI2
from activos.views import AnexoTextoAPI
from activos.views import AnexoArchivoAPI
from activos.views import AnexoImagenAPI
from activos.views import OdometroAPI
from activos.views import UdmOdometroAPI
from activos.views import UdmOdometroAPI2
from activos.views import MedicionAPI

from inventarios.views import AlmacenAPI
from inventarios.views import UdmArticuloAPI
from inventarios.views import UdmArticuloAPI2
from inventarios.views import ArticuloAPI
from inventarios.views import ArticuloAPI2
from inventarios.views import ArticuloAnexoTextoAPI
from inventarios.views import ArticuloAnexoImagenAPI
from inventarios.views import ArticuloAnexoArchivoAPI
from inventarios.views import StockAPI
from inventarios.views import MovimientoAPI
from inventarios.views import MovimientoDetalleAPI

from trabajos.views import OrdenTrabajoAPI
from trabajos.views import OrdenTrabajoLastAPI
from trabajos.views import OrdenAnexoTextoAPI
from trabajos.views import OrdenAnexoImagenAPI
from trabajos.views import OrdenAnexoArchivoAPI
from trabajos.views import ActividadAPI
from trabajos.views import ManoObraAPI
from trabajos.views import MaterialAPI
from trabajos.views import ServicioExternoAPI

from seguridad.views import UserAPI

# Librerias necesarias para publicar Medias en DEBUG
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()


# ----------------- EQUIPOS ----------------- #

router.register(
    r'equipos',
    EquipoAPI,
    'equipo'
)

# ----------------- USUARIOS ----------------- #

router.register(
    r'users',
    UserAPI,
    'user'
)

# ----------------- EQUIPOS - ANEXOS ----------------- #

router.register(
    r'anexostexto',
    AnexoTextoAPI,
    'anexotexto'
)
router.register(
    r'anexosarchivo',
    AnexoArchivoAPI,
    'anexoarchivo'
),
router.register(
    r'anexosimagen',
    AnexoImagenAPI,
    'anexoimagen'
)

# ----------------- UBICACIONES ----------------- #

router.register(
    r'ubicaciones',
    UbicacionAPI,
    'ubicacion'
)
router.register(
    r'ubicaciones2',
    UbicacionAPI2,
    'ubicacion2'
)


# ----------------- ODOMETROS ----------------- #

router.register(
    r'odometros',
    OdometroAPI,
    'odometro'
)

# ----------------- UDMS - ODOMETRO ----------------- #

router.register(
    r'udmodometro',
    UdmOdometroAPI,
    'udmodometro'
)
router.register(
    r'udmodometro2',
    UdmOdometroAPI2,
    'udmodometro2'
)


# ----------------- MEDICIONES ----------------- #

router.register(
    r'mediciones',
    MedicionAPI,
    'medicion'
)


# ----------------- ALMACENES ----------------- #

router.register(
    r'almacenes',
    AlmacenAPI,
    'almacen'
)

# ----------------- ARTICULO - UDM ----------------- #

router.register(
    r'udmarticulo',
    UdmArticuloAPI,
    'udmarticulo'
)
router.register(
    r'udmarticulo2',
    UdmArticuloAPI2,
    'udmarticulo2'
)

# ----------------- ARTICULOS ----------------- #

router.register(
    r'articulos',
    ArticuloAPI,
    'articulo'
)

router.register(
    r'articulos2',
    ArticuloAPI2,
    'articulo2'
)


# ----------------- STOCK ----------------- #
router.register(
    r'stock',
    StockAPI,
    'stock'
)


# ----------------- ARTICULOS - ANEXOS ----------------- #

router.register(
    r'articulosanexotexto',
    ArticuloAnexoTextoAPI,
    'articuloanexotexto'
)
router.register(
    r'articulosanexoimagen',
    ArticuloAnexoImagenAPI,
    'articuloanexoimagen'
)
router.register(
    r'articulosanexoarchivo',
    ArticuloAnexoArchivoAPI,
    'articuloanexoarchivo'
)


# ----------------- ORDENES DE TRABAJO ----------------- #

router.register(
    r'ordenestrabajo',
    OrdenTrabajoAPI,
    'ordentrabajo'
)


router.register(
    r'ordenestrabajolast',
    OrdenTrabajoLastAPI,
    'ordentrabajolast'
)

# ----------------- ACTIVIDAD ----------------- #

router.register(
    r'actividades',
    ActividadAPI,
    'actividad'
)

# ----------------- MANO OBRA ----------------- #

router.register(
    r'manoobra',
    ManoObraAPI,
    'manoobra'
)


# ----------------- MATERIAL ----------------- #

router.register(
    r'materiales',
    MaterialAPI,
    'material'
)


# ----------------- SERVICIO EXTERNO ----------------- #

router.register(
    r'servicioexterno',
    ServicioExternoAPI,
    'servicioexterno'
)


# ----------------- ORDENES DE TRABAJO - ANEXOS ----------------- #

router.register(
    r'ordenesanexotexto',
    OrdenAnexoTextoAPI,
    'ordenanexotexto'
)
router.register(
    r'ordenesanexoimagen',
    OrdenAnexoImagenAPI,
    'ordenanexoimagen'
)
router.register(
    r'ordenesanexoarchivo',
    OrdenAnexoArchivoAPI,
    'ordenanexoarchivo'
)

# ----------------- ENTRADAS  ----------------- #

router.register(
    r'movimientos',
    MovimientoAPI,
    'movimientocabecera'
)

router.register(
    r'movimientosdetalle',
    MovimientoDetalleAPI,
    'movimientodetalle'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'', include('seguridad.urls', namespace="seguridad")),
    url(r'', include('activos.urls', namespace="activos")),
    url(r'', include('inventarios.urls', namespace="inventarios")),
    url(r'', include('trabajos.urls', namespace="trabajos")),
    url(r'', include('dashboards.urls', namespace="dashboards")),
]


if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
