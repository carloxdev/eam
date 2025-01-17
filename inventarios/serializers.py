# -*- coding: utf-8 -*-

# API REST:
from rest_framework import serializers

# Modelos:
from .models import Almacen
from .models import Stock
from .models import Articulo
from .models import MovimientoCabecera
from .models import MovimientoDetalle
from .models import UdmArticulo


# ----------------- ALMACEN ----------------- #

class AlmacenSerializer(serializers.ModelSerializer):

    estado = serializers.SerializerMethodField()

    class Meta:
        model = Almacen
        fields = (
            'url',
            'pk',
            'clave',
            'descripcion',
            'estado',
            'empresa',
        )

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""


# ----------------- STOCK ----------------- #

class StockSerializer(serializers.ModelSerializer):

    almacen = serializers.SerializerMethodField()
    articulo = serializers.SerializerMethodField()
    udm = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = (
            'url',
            'pk',
            'almacen',
            'articulo',
            'cantidad',
            'udm'
        )

    def get_almacen(self, obj):

        try:
            return "({}) {}".format(
                obj.almacen.clave,
                obj.almacen.descripcion
            )

        except:
            return ""

    def get_articulo(self, obj):

        try:
            return "({}) {}".format(
                obj.articulo.clave,
                obj.articulo.descripcion
            )

        except:
            return ""

    def get_udm(self, obj):

        try:
            return "{}".format(
                obj.articulo.udm,
            )

        except:
            return ""


# ----------------- UDM ODOMETRO ----------------- #

class UdmArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = UdmArticulo
        fields = (
            'pk',
            'url',
            'clave',
            'descripcion'
        )


# ----------------- ARTICULO ----------------- #

class ArticuloSerializer(serializers.HyperlinkedModelSerializer):

    tipo = serializers.SerializerMethodField()
    udm = serializers.SerializerMethodField()
    estado = serializers.SerializerMethodField()

    class Meta:
        model = Articulo
        fields = (
            'url',
            'pk',
            'clave',
            'descripcion',
            'tipo',
            'estado',
            'udm',
            'clave_jde',
        )

    def get_tipo(self, obj):
        try:
            return obj.get_tipo_display()
        except:
            return ""

    def get_udm(self, obj):

        try:
            return "({}) {}".format(
                obj.udm.clave,
                obj.udm.descripcion
            )

        except:
            return ""

    def get_estado(self, obj):
        try:
            return obj.get_estado_display()
        except:
            return ""


# ----------------- ENTRADA ----------------- #

class MovimientoCabeceraSerializer(serializers.HyperlinkedModelSerializer):
    estado = serializers.SerializerMethodField()
    almacen_origen = serializers.SerializerMethodField()
    almacen_destino = serializers.SerializerMethodField()
    clasificacion = serializers.SerializerMethodField()
    orden_trabajo = serializers.SerializerMethodField()

    class Meta:
        model = MovimientoCabecera
        fields = (
            'pk',
            'url',
            'fecha',
            'descripcion',
            'almacen_origen',
            'almacen_destino',
            'persona_recibe',
            'persona_entrega',
            'tipo',
            'estado',
            'clasificacion',
            'orden_trabajo',
            'usuario',
        )

    def get_estado(self, obj):

        try:
            return obj.get_estado_display()
        except:
            return ""

    def get_almacen_origen(self, obj):

        try:
            return "({}) {}".format(
                obj.almacen_origen.clave.encode("utf-8"),
                obj.almacen_origen.descripcion.encode("utf-8")
            )
        except:
            return ""

    def get_almacen_destino(self, obj):

        try:
            return "({}) {}".format(
                obj.almacen_destino.clave.encode("utf-8"),
                obj.almacen_destino.descripcion.encode("utf-8")
            )
        except:
            return ""

    def get_clasificacion(self, obj):
        try:
            return obj.get_clasificacion.display()
        except:
            return ""

    def get_orden_trabajo(self, obj):
        try:
            return "{} - {}".format(
                obj.orden_trabajo.clave.encode("utf-8"),
                obj.orden_trabajo.descripcion.encode("utf-8")
            )
        except:
            return ""


class MovimientoDetalleSerializer(serializers.ModelSerializer):

    articulo_clave = serializers.SerializerMethodField()

    class Meta:
        model = MovimientoDetalle
        fields = (
            'pk',
            'url',
            'cantidad',
            'articulo',
            'cabecera',
            'articulo_clave',
        )

    def get_articulo_clave(self, obj):

        try:
            return "({}) {}".format(
                obj.articulo.clave.encode("utf-8"),
                obj.articulo.descripcion.encode("utf-8")
            )
        except:
            return ""
