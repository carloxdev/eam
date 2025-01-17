# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas:
from .views import AlmacenListView
from .views import AlmacenCreateView
from .views import AlmacenUpdateView

from .views import StockListView

from .views import UdmArticuloListView
from .views import UdmArticuloCreateView
from .views import UdmArticuloUpdateView

from .views import ArticuloListView
from .views import ArticuloCreateView
from .views import ArticuloUpdateView

from .views import ArticuloAnexoTextoView
from .views import ArticuloAnexoImagenView
from .views import ArticuloAnexoArchivoView

from .views import EntradaListView
from .views import EntradaCabeceraCreateView
from .views import EntradaCabeceraUpdateView
from .views import SalidaListView
from .views import SalidaCabeceraCreateView
from .views import SalidaCabeceraUpdateView
from .views import EntradaSaldoListView
from .views import EntradaSaldoCreateView
from .views import EntradaSaldoUpdateView
from .views import EntradaCompraListView
from .views import EntradaCompraCreateView
from .views import EntradaCompraUpdateView

app_name = "inventarios"

urlpatterns = [

    # ----------------- ALMACEN ----------------- #

    url(
        r'^almacenes/$',
        AlmacenListView.as_view(),
        name='almacenes_lista'
    ),
    url(
        r'^almacenes/nuevo/$',
        AlmacenCreateView.as_view(),
        name='almacenes_nuevo'
    ),
    url(
        r'^almacenes/editar/(?P<pk>.*)/$',
        AlmacenUpdateView.as_view(),
        name='almacenes_editar'
    ),


    # ----------------- UDM ARTICULO ----------------- #

    url(
        r'udmarticulo/$',
        UdmArticuloListView.as_view(),
        name='udms_articulo_lista'
    ),
    url(
        r'udmarticulo/nuevo/$',
        UdmArticuloCreateView.as_view(),
        name='udms_articulo_nuevo'
    ),
    url(
        r'udmarticulo/editar/(?P<pk>\d+)/$',
        UdmArticuloUpdateView.as_view(),
        name='udms_articulo_editar'
    ),



    # ----------------- ARTICULOS ----------------- #

    url(
        r'^articulos/$',
        ArticuloListView.as_view(),
        name='articulos_lista'
    ),
    url(
        r'^articulos/nuevo/$',
        ArticuloCreateView.as_view(),
        name='articulos_nuevo'
    ),
    url(
        r'^articulos/editar/(?P<pk>.*)/$',
        ArticuloUpdateView.as_view(),
        name='articulos_editar'
    ),


    # ----------------- ARTICULOS - ANEXOS ----------------- #

    url(
        r'articulos/anexos/(?P<pk>\d+)/texto/$',
        ArticuloAnexoTextoView.as_view(),
        name='anexar_texto'
    ),
    url(
        r'^articulos/anexos/(?P<pk>\d+)/imagen/$',
        ArticuloAnexoImagenView.as_view(),
        name='anexar_imagen'
    ),
    url(
        r'^articulos/anexos/(?P<pk>\d+)/archivo/$',
        ArticuloAnexoArchivoView.as_view(),
        name='anexar_archivo'
    ),


    # ----------------- STOCK ----------------- #

    url(
        r'^stock/(?P<almacen>\d+)/(?P<articulo>\d+)/$',
        StockListView.as_view(),
        name='stock'
    ),


    # ----------------- ENTRADAS ----------------- #

    url(
        r'entradas/$',
        EntradaListView.as_view(),
        name='entradas_lista'
    ),
    url(
        r'entradas/nuevo/$',
        EntradaCabeceraCreateView.as_view(),
        name='entradas_nuevo'
    ),
    url(
        r'entradas/editar/(?P<pk>\d+)/$',
        EntradaCabeceraUpdateView.as_view(),
        name='entradas_editar'
    ),
    url(
        r'entradas/saldo_inicial/$',
        EntradaSaldoListView.as_view(),
        name='entradas_saldoinicial_lista'
    ),
    url(
        r'entradas/saldo_inicial/nuevo/$',
        EntradaSaldoCreateView.as_view(),
        name='entradas_saldoinicial_nuevo'
    ),
    url(
        r'entradas/saldo_inicial/editar/(?P<pk>\d+)/$',
        EntradaSaldoUpdateView.as_view(),
        name='entradas_saldoinicial_editar'
    ),
    url(
        r'entradas/compras/$',
        EntradaCompraListView.as_view(),
        name='entradas_compras_lista'
    ),
    url(
        r'entradas/saldo_inicial/nuevo/$',
        EntradaCompraCreateView.as_view(),
        name='entradas_compras_nuevo'
    ),
    url(
        r'entradas/saldo_inicial/editar/(?P<pk>\d+)/$',
        EntradaCompraUpdateView.as_view(),
        name='entradas_compras_editar'
    ),
    # ----------------- SALIDAS ----------------- #
    url(
        r'salidas/$',
        SalidaListView.as_view(),
        name='salidas_lista'
    ),
    url(
        r'salidas/nuevo/$',
        SalidaCabeceraCreateView.as_view(),
        name='salidas_nuevo'
    ),
    url(
        r'salidas/editar/(?P<pk>\d+)/$',
        SalidaCabeceraUpdateView.as_view(),
        name='salidas_editar'
    ),
]
