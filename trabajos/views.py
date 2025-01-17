# -*- coding: utf-8 -*-

# Django Atajos:
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse

# Django Generic Views
from django.views.generic.base import View

# Modelos:
from .models import OrdenTrabajo
from .models import Actividad
from .models import ManoObra
from .models import Material
from .models import ServicioExterno

from home.models import AnexoTexto
from home.models import AnexoImagen
from home.models import AnexoArchivo

# Formularios:
from .forms import OrdenTrabajoForm
from home.forms import AnexoTextoForm
from home.forms import AnexoImagenForm
from home.forms import AnexoArchivoForm

# API Rest & Json:
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# API Rest - Serializadores:
from .serializers import OrdenTrabajoSerializer
from .serializers import ActividadSerializer

from .serializers import ManoObraSerializer
from .serializers import MaterialSerializer
from .serializers import ServicioExternoSerializer

from home.serializers import AnexoTextoSerializer
from home.serializers import AnexoImagenSerializer
from home.serializers import AnexoArchivoSerializer


# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import OrdenTrabajoFilter

# Formulario Filtros
from .forms import OrdenTrabajoFiltersForm


# ----------------- ORDEN DE TRABAJO ----------------- #


class OrdenTrabajoListView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/lista.html'

    def get(self, _request):
        formulario = OrdenTrabajoFiltersForm()
        contexto = {
            'form': formulario
        }
        return render(_request, self.template_name, contexto)


class OrdenTrabajoCreateView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/formulario.html'

    def get(self, request):
        formulario = OrdenTrabajoForm()

        contexto = {
            'form': formulario,
            'operation': "Nueva"
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = OrdenTrabajoForm(request.POST)

        if formulario.is_valid():

            datos_formulario = formulario.cleaned_data
            orden = OrdenTrabajo()

            orden.equipo = datos_formulario.get('equipo')
            orden.descripcion = datos_formulario.get('descripcion')
            orden.tipo = datos_formulario.get('tipo')
            orden.estado = datos_formulario.get('estado')
            orden.responsable = datos_formulario.get('responsable')
            orden.fecha_estimada_inicio = datos_formulario.get(
                'fecha_estimada_inicio'
            )
            orden.fecha_estimada_fin = datos_formulario.get(
                'fecha_estimada_fin'
            )
            orden.fecha_real_inicio = datos_formulario.get('fecha_real_inicio')
            orden.fecha_real_fin = datos_formulario.get('fecha_real_fin')
            orden.observaciones = datos_formulario.get('observaciones')
            orden.es_template = datos_formulario.get('es_template')

            orden.save()

            return redirect(
                reverse(
                    'trabajos:actividades_lista',
                    kwargs={'pk': orden.id}
                )
            )

        contexto = {
            'form': formulario,
            'operation': "Nueva"
        }

        return render(request, self.template_name, contexto)


class OrdenTrabajoUpdateView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/formulario.html'

    def get(self, request, pk):

        orden = get_object_or_404(OrdenTrabajo, pk=pk)

        formulario = OrdenTrabajoForm(
            initial={
                'equipo': orden.equipo,
                'descripcion': orden.descripcion,
                'tipo': orden.tipo,
                'estado': orden.estado,
                'responsable': orden.responsable,
                'fecha_estimada_inicio': orden.fecha_estimada_inicio,
                'fecha_estimada_fin': orden.fecha_estimada_fin,
                'fecha_real_inicio': orden.fecha_real_inicio,
                'fecha_real_fin': orden.fecha_real_fin,
                'observaciones': orden.observaciones,
                'es_template': orden.es_template,
            }
        )

        contexto = {
            'form': formulario,
            'operation': "Editar",
            'orden': orden
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        formulario = OrdenTrabajoForm(request.POST)

        orden = get_object_or_404(OrdenTrabajo, pk=pk)

        if formulario.is_valid():

            datos_formulario = formulario.cleaned_data

            orden.equipo = datos_formulario.get('equipo')
            orden.descripcion = datos_formulario.get('descripcion')
            orden.tipo = datos_formulario.get('tipo')
            orden.estado = datos_formulario.get('estado')
            orden.responsable = datos_formulario.get('responsable')
            orden.fecha_estimada_inicio = datos_formulario.get(
                'fecha_estimada_inicio'
            )
            orden.fecha_estimada_fin = datos_formulario.get(
                'fecha_estimada_fin'
            )
            orden.fecha_real_inicio = datos_formulario.get('fecha_real_inicio')
            orden.fecha_real_fin = datos_formulario.get('fecha_real_fin')
            orden.observaciones = datos_formulario.get('observaciones')
            orden.es_template = datos_formulario.get('es_template')

            orden.save()

            return redirect(
                reverse(
                    'trabajos:actividades_lista',
                    kwargs={'pk': orden.id}
                )
            )

        contexto = {
            'form': formulario,
            'operation': "Editar",
            'orden': orden
        }

        return render(request, self.template_name, contexto)


class OrdenTrabajoAPI(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = OrdenTrabajoFilter


class OrdenTrabajoLastAPI(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.order_by('created_date')[:10]
    serializer_class = OrdenTrabajoSerializer


# ----------------- ACTIVIDAD ----------------- #

class ActividadListView(View):

    def __init__(self):
        self.template_name = 'actividad/lista.html'

    def get(self, _request, pk):

        orden = get_object_or_404(OrdenTrabajo, pk=pk)

        formulario = OrdenTrabajoForm(
            initial={
                'equipo': orden.equipo,
                'descripcion': orden.descripcion,
                'tipo': orden.tipo,
                'estado': orden.estado,
            }
        )

        formulario.fields['equipo'].widget.attrs['disabled'] = True
        formulario.fields['descripcion'].widget.attrs['disabled'] = True
        formulario.fields['tipo'].widget.attrs['disabled'] = True
        formulario.fields['estado'].widget.attrs['disabled'] = True

        contexto = {
            'form': formulario,
            'orden': orden
        }

        return render(_request, self.template_name, contexto)


class ActividadAPI(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden', 'id')


# ----------------- MANO OBRA ----------------- #

class ManoObraListView(View):

    def __init__(self):
        self.template_name = 'mano_obra/lista.html'

    def get(self, _request, pk):

        orden = get_object_or_404(OrdenTrabajo, pk=pk)

        formulario = OrdenTrabajoForm(
            initial={
                'equipo': orden.equipo,
                'descripcion': orden.descripcion,
                'tipo': orden.tipo,
                'estado': orden.estado,
            }
        )

        formulario.fields['equipo'].widget.attrs['disabled'] = True
        formulario.fields['descripcion'].widget.attrs['disabled'] = True
        formulario.fields['tipo'].widget.attrs['disabled'] = True
        formulario.fields['estado'].widget.attrs['disabled'] = True

        contexto = {
            'form': formulario,
            'orden': orden
        }

        return render(_request, self.template_name, contexto)


class ManoObraAPI(viewsets.ModelViewSet):
    queryset = ManoObra.objects.all()
    serializer_class = ManoObraSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden', 'id')


# ----------------- MATERIAL ----------------- #

class MaterialListView(View):

    def __init__(self):
        self.template_name = 'material/lista.html'

    def get(self, _request, pk):

        orden = get_object_or_404(OrdenTrabajo, pk=pk)

        formulario = OrdenTrabajoForm(
            initial={
                'equipo': orden.equipo,
                'descripcion': orden.descripcion,
                'tipo': orden.tipo,
                'estado': orden.estado,
            }
        )

        formulario.fields['equipo'].widget.attrs['disabled'] = True
        formulario.fields['descripcion'].widget.attrs['disabled'] = True
        formulario.fields['tipo'].widget.attrs['disabled'] = True
        formulario.fields['estado'].widget.attrs['disabled'] = True

        contexto = {
            'form': formulario,
            'orden': orden
        }

        return render(_request, self.template_name, contexto)


class MaterialAPI(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden', 'id')


# ----------------- SERVICIO EXTERNO ----------------- #

class ServicioExternoListView(View):

    def __init__(self):
        self.template_name = 'servicio_externo/lista.html'

    def get(self, _request, pk):

        orden = get_object_or_404(OrdenTrabajo, pk=pk)

        formulario = OrdenTrabajoForm(
            initial={
                'equipo': orden.equipo,
                'descripcion': orden.descripcion,
                'tipo': orden.tipo,
                'estado': orden.estado,
            }
        )

        formulario.fields['equipo'].widget.attrs['disabled'] = True
        formulario.fields['descripcion'].widget.attrs['disabled'] = True
        formulario.fields['tipo'].widget.attrs['disabled'] = True
        formulario.fields['estado'].widget.attrs['disabled'] = True

        contexto = {
            'form': formulario,
            'orden': orden
        }

        return render(_request, self.template_name, contexto)


class ServicioExternoAPI(viewsets.ModelViewSet):
    queryset = ServicioExterno.objects.all()
    serializer_class = ServicioExternoSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden', 'id')


# ----------------- ORDEN - ANEXO ----------------- #


class OrdenAnexoTextoView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/anexos/anexos_texto.html'

    def get(self, request, pk):
        id_orden = pk
        anexos = AnexoTexto.objects.filter(orden_trabajo=id_orden)
        orden_trabajo = OrdenTrabajo.objects.get(id=id_orden)
        form = AnexoTextoForm()

        contexto = {
            'form': form,
            'id': id_orden,
            'orden_trabajo': orden_trabajo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_orden = pk
        form = AnexoTextoForm(request.POST)
        anexos = AnexoTexto.objects.filter(orden_trabajo=id_orden)
        orden_trabajo = OrdenTrabajo.objects.get(id=id_orden)

        if form.is_valid():
            texto = form.save(commit=False)
            texto.orden_trabajo_id = id_orden
            texto.save()
            anexos = AnexoTexto.objects.filter(orden_trabajo=id_orden)
            form = AnexoTextoForm()
        return render(request, 'orden_trabajo/anexos/anexos_texto.html',
                      {'form': form, 'id': id_orden, 'anexos': anexos,
                       'orden_trabajo': orden_trabajo})


class OrdenAnexoImagenView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/anexos/anexos_imagen.html'

    def get(self, request, pk):
        id_orden = pk
        anexos = AnexoImagen.objects.filter(orden_trabajo=id_orden)
        orden_trabajo = OrdenTrabajo.objects.get(id=id_orden)
        form = AnexoImagenForm()

        contexto = {
            'form': form,
            'id': id_orden,
            'orden_trabajo': orden_trabajo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_orden = pk
        anexos = AnexoImagen.objects.filter(orden_trabajo=id_orden)
        orden_trabajo = OrdenTrabajo.objects.get(id=id_orden)
        form = AnexoImagenForm(request.POST, request.FILES)

        if form.is_valid():

            imagen_anexo = AnexoImagen()
            imagen_anexo.descripcion = request.POST['descripcion']
            if 'ruta' in request.POST:
                imagen_anexo.ruta = request.POST['ruta']
            else:
                imagen_anexo.ruta = request.FILES['ruta']
            imagen_anexo.orden_trabajo_id = id_orden
            imagen_anexo.save()
            form = AnexoImagenForm()
            anexos = AnexoImagen.objects.filter(orden_trabajo=id_orden)

        contexto = {
            'form': form,
            'id': id_orden,
            'anexos': anexos,
            'orden_trabajo': orden_trabajo,

        }
        return render(request, self.template_name, contexto)


class OrdenAnexoArchivoView(View):

    def __init__(self):
        self.template_name = 'orden_trabajo/anexos/anexos_archivo.html'

    def get(self, request, pk):
        id_orden = pk
        anexos = AnexoArchivo.objects.filter(orden_trabajo=id_orden)
        orden_trabajo = OrdenTrabajo.objects.get(id=id_orden)
        form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_orden,
            'orden_trabajo': orden_trabajo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_orden = pk
        orden_trabajo = OrdenTrabajo.objects.get(id=id_orden)
        form = AnexoArchivoForm(request.POST, request.FILES)
        anexos = AnexoArchivo.objects.filter(orden_trabajo=id_orden)

        if form.is_valid():
            archivo_anexo = AnexoArchivo()
            archivo_anexo.descripcion = request.POST['descripcion']
            if 'archivo' in request.POST:
                archivo_anexo.archivo = request.POST['archivo']
            else:
                archivo_anexo.archivo = request.FILES['archivo']
            archivo_anexo.orden_trabajo_id = id_orden
            archivo_anexo.save()
            anexos = AnexoArchivo.objects.filter(orden_trabajo=id_orden)
            form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_orden,
            'orden_trabajo': orden_trabajo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)


class OrdenAnexoTextoAPI(viewsets.ModelViewSet):
    queryset = AnexoTexto.objects.all()
    serializer_class = AnexoTextoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden_trabajo',)


class OrdenAnexoImagenAPI(viewsets.ModelViewSet):
    queryset = AnexoImagen.objects.all()
    serializer_class = AnexoImagenSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden_trabajo',)


class OrdenAnexoArchivoAPI(viewsets.ModelViewSet):
    queryset = AnexoArchivo.objects.all()
    serializer_class = AnexoArchivoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('orden_trabajo',)
