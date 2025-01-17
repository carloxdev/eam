# -*- coding: utf-8 -*-

# Librerias Django:
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from django.contrib.auth.models import User
from activos.models import Equipo
from inventarios.models import Articulo

# Historia
from simple_history.models import HistoricalRecords


class OrdenTrabajo(models.Model):

    ORDEN_TIPO = (
        ('PREVE', 'PREVENTIVA'),
        ('PREDI', 'PREDICTIVA'),
        ('CORRE', 'CORRECTIVA'),
    )

    ORDEN_ESTADO = (
        ('CAP', 'ABIERTA'),
        ('TER', 'TERMINADA'),
        ('CER', 'CERRADA'),
    )

    equipo = models.ForeignKey(Equipo)
    descripcion = models.CharField(max_length=144, null=True)
    tipo = models.CharField(
        max_length=6,
        choices=ORDEN_TIPO,
        default="CORRE",
    )

    estado = models.CharField(
        max_length=5,
        choices=ORDEN_ESTADO,
        default="CAP",
    )

    responsable = models.CharField(max_length=144, null=True, blank=True)
    fecha_estimada_inicio = models.DateTimeField(null=True, blank=True)
    fecha_estimada_fin = models.DateTimeField(null=True, blank=True)
    fecha_real_inicio = models.DateTimeField(null=True, blank=True)
    fecha_real_fin = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    es_template = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return "{0} : {1}".format(self.equipo, self.id).encode('utf-8')

    class Meta:
        verbose_name_plural = "Ordenes de Trabajo"


class Actividad(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=144, null=True)
    horas_estimadas = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0
    )
    horas_reales = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.numero)

    class Meta:
        verbose_name_plural = "Actividades"
        unique_together = (('orden', 'numero'),)


class ManoObra(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    empleado = models.ForeignKey(User, null=True)
    descripcion = models.CharField(max_length=144, null=True, blank=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    horas_estimadas = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0,
        blank=True
    )
    horas_reales = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.0,
        blank=True
    )
    costo = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0, blank=True
    )

    # Auditoria Fields
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.empleado)

    class Meta:
        verbose_name_plural = "Mano de Obra"
        unique_together = (('orden', 'empleado'),)


class Material(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    articulo = models.ForeignKey(Articulo)
    cantidad_estimada = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    cantidad_real = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    costo = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0, blank=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.articulo)

    class Meta:
        verbose_name_plural = "Materiales"
        unique_together = (('orden', 'articulo'),)


class ServicioExterno(models.Model):
    orden = models.ForeignKey(OrdenTrabajo)
    descripcion = models.CharField(max_length=144, null=True)
    clave_jde = models.CharField(max_length=144, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    costo = models.DecimalField(
        max_digits=20, decimal_places=4, default=0.0, blank=True
    )
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return "{0} : {1}".format(self.orden, self.clave_jde)

    class Meta:
        verbose_name_plural = "Servicios Externos"
