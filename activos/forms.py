# -*- coding: utf-8 -*-

# Django:
from django.forms import ModelForm
from django.forms import TextInput
from django.forms import Select
from django.forms import CheckboxInput

# Modelos:
from .models import Equipo
from .models import Odometro
from .models import Medicion
from .models import Ubicacion
from .models import UdmOdometro


# ----------------- EQUIPO ----------------- #

class EquipoFiltersForm(ModelForm):

    class Meta:
        model = Equipo
        fields = [
            'tag',
            'descripcion',
            'serie',
            'estado',
            'empresa',
            'padre',
            'sistema',
            'ubicacion',
        ]
        widgets = {
            'tag': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'serie': TextInput(attrs={'class': 'form-control input-sm'}),
            'estado': Select(attrs={'class': 'form-control input-sm select2'}),
            'empresa': Select(
                attrs={'class': 'form-control input-sm select2'}
            ),
            'padre': Select(attrs={'class': 'form-control input-sm select2'}),
            'sistema': TextInput(attrs={'class': 'form-control input-sm'}),
            'ubicacion': Select(
                attrs={'class': 'form-control input-sm select2'}
            ),
        }
        labels = {
            'tag': 'Tag',
            'descripcion': 'Descripción',
            'serie': 'Serie',
            'estado': 'Estado',
            'padre': 'Padre',
            'empresa': 'Empresa',
            'sistema': 'Sistema',
            'ubicacion': 'Ubicación',
        }


class EquipoForm(ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'tag': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'serie': TextInput(attrs={'class': 'form-control input-sm'}),
            'tipo': TextInput(attrs={'class': 'form-control input-sm'}),
            'estado': Select(attrs={'class': 'form-control input-sm select2'}),
            'padre': Select(attrs={'class': 'form-control input-sm select2'}),
            'empresa': Select(
                attrs={'class': 'form-control input-sm select2'}
            ),
            'sistema': TextInput(attrs={'class': 'form-control input-sm'}),
            'ubicacion': Select(
                attrs={'class': 'form-control input-sm select2'}
            ),
            'cliente': TextInput(attrs={'class': 'form-control input-sm'}),
            'responsable': TextInput(attrs={'class': 'form-control input-sm'}),
        }
        labels = {
            'tag': 'Tag',
            'descripcion': 'Descripción',
            'serie': 'Serie',
            'tipo': 'Tipo',
            'estado': 'Estado',
            'padre': 'Padre',
            'empresa': 'Empresa',
            'sistema': 'Sistema',
            'ubicacion': 'Ubicación',
            'imagen': 'Imagen',
            'cliente': 'Cliente',
            'responsable': 'Responsable',
        }


# ----------------- ODÓMETRO ----------------- #

class OdometroForm(ModelForm):

    class Meta:
        model = Odometro
        fields = [
            'equipo',
            'clave',
            'descripcion',
            'udm',
            'esta_activo',
        ]
        widgets = {
            'equipo': Select(attrs={'class': 'form-control input-sm select2'}),
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'udm': Select(attrs={'class': 'form-control input-sm select2'}),
            'esta_activo': CheckboxInput(),
        }
        labels = {
            'equipo': 'Equipo',
            'clave': 'Clave',
            'descripcion': 'Descripción',
            'udm': 'UDM',
            'esta_activo': 'Activo',
        }


class OdometroFiltersForm(ModelForm):

    class Meta:
        model = Odometro
        fields = [
            'equipo',
            'clave',
            'descripcion',
            'udm',
        ]
        widgets = {
            'equipo': Select(attrs={'class': 'form-control input-sm select2'}),
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
            'udm': Select(attrs={'class': 'form-control input-sm select2'}),
        }
        labels = {
            'equipo': 'Equipo',
            'clave': 'Clave',
            'descripcion': 'Descripción',
            'udm': 'UDM',
        }


# ----------------- UDM ODOMETRO ----------------- #

class UdmOdometroForm(ModelForm):

    class Meta:
        model = UdmOdometro
        fields = '__all__'
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
        }


# ----------------- MEDICION ----------------- #

class MedicionFiltersForm(ModelForm):

    class Meta:
        model = Medicion
        fields = [
            'odometro',
        ]
        widgets = {
            'odometro': Select(
                attrs={'class': 'form-control input-sm select2'}
            ),
        }
        labels = {
            'odometro': 'Odómetro',
        }


class MedicionForm(ModelForm):

    class Meta:
        model = Medicion
        fields = [
            'fecha',
            'lectura'
        ]
        widgets = {
            'fecha': TextInput(
                attrs={
                    'class': 'form-control input-sm pull-right',
                    'data-date-format': 'yyyy-mm-dd'
                }
            ),
            'lectura': TextInput(attrs={'class': 'form-control input-sm'}),
        }
        labels = {
            'fecha': 'Fecha',
            'lectura': 'Lectura',
        }


# ----------------- UBICACION ----------------- #

class UbicacionForm(ModelForm):

    class Meta:
        model = Ubicacion
        fields = '__all__'
        widgets = {
            'clave': TextInput(attrs={'class': 'form-control input-sm'}),
            'descripcion': TextInput(attrs={'class': 'form-control input-sm'}),
        }
