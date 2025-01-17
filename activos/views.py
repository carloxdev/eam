# -*- coding: utf-8 -*-

# Django Atajos:
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Django Urls:
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

# Django Generic Views
from django.views.generic.base import View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import TemplateView

# Modelos:
from .models import Equipo
from .models import Odometro
from .models import Ubicacion
from .models import Medicion
from .models import UdmOdometro
from home.models import AnexoImagen
from home.models import AnexoArchivo
from home.models import AnexoTexto

# Formularios:
from .forms import EquipoFiltersForm
from .forms import EquipoForm
from .forms import UbicacionForm
from .forms import OdometroForm
from .forms import OdometroFiltersForm
from .forms import MedicionFiltersForm
from .forms import MedicionForm
from .forms import UdmOdometroForm
from home.forms import AnexoTextoForm
from home.forms import AnexoImagenForm
from home.forms import AnexoArchivoForm

# API Rest:
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# API Rest - Serializadores:
from .serializers import EquipoSerializer
from .serializers import EquipoTreeSerilizado
from .serializers import UbicacionSerializer
from .serializers import OdometroSerializer
from .serializers import MedicionSerializer
from .serializers import UdmOdometroSerializer
from home.serializers import AnexoTextoSerializer
from home.serializers import AnexoArchivoSerializer
from home.serializers import AnexoImagenSerializer

# API Rest - Paginacion:
from .pagination import GenericPagination

# API Rest - Filtros:
from .filters import EquipoFilter
from .filters import OdometroFilter
from .filters import MedicionFilter


# ----------------- EQUIPO ----------------- #

class EquipoListView(View):

    def __init__(self):
        self.template_name = 'equipo/lista.html'

    def get(self, request):

        formulario = EquipoFiltersForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)


class EquipoCreateView(View):

    def __init__(self):
        self.template_name = 'equipo/formulario.html'

    def obtener_UrlImagen(self, _imagen):
        imagen = ''

        if _imagen:
            imagen = _imagen.url

        return imagen

    def get(self, request):
        formulario = EquipoForm()
        contexto = {
            'form': formulario,
            'operation': "Nuevo"
        }

        return render(request, self.template_name, contexto)

    def post(self, request):

        formulario = EquipoForm(request.POST, request.FILES)

        if formulario.is_valid():

            datos_formulario = formulario.cleaned_data
            equipo = Equipo()
            equipo.tag = datos_formulario.get('tag')
            equipo.descripcion = datos_formulario.get('descripcion')
            equipo.serie = datos_formulario.get('serie')
            equipo.tipo = datos_formulario.get('tipo')
            equipo.estado = datos_formulario.get('estado')
            equipo.padre = datos_formulario.get('padre')
            equipo.empresa = datos_formulario.get('empresa')
            equipo.sistema = datos_formulario.get('sistema')
            equipo.ubicacion = datos_formulario.get('ubicacion')
            equipo.imagen = datos_formulario.get('imagen')

            equipo.save()

            return redirect(
                reverse('activos:equipos_lista')
            )

        contexto = {
            'form': formulario,
            'imagen': self.obtener_UrlImagen(equipo.imagen),
            'operation': "Nuevo"
        }
        return render(request, self.template_name, contexto)


class EquipoUpdateView(View):

    def __init__(self):
        self.template_name = 'equipo/formulario.html'
        self.tag = ''

    def obtener_UrlImagen(self, _imagen):
        imagen = ''

        if _imagen:
            imagen = _imagen.url

        return imagen

    def get(self, request, pk):

        equipo = get_object_or_404(Equipo, pk=pk)
        self.tag = equipo.tag

        formulario = EquipoForm(
            instance=equipo
        )

        contexto = {
            'form': formulario,
            'tag': self.tag,
            'operation': "Editar",
            'equipo_id': equipo.id,
            'imagen': self.obtener_UrlImagen(equipo.imagen)
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):

        equipo = get_object_or_404(Equipo, pk=pk)
        self.tag = equipo.tag

        formulario = EquipoForm(request.POST, request.FILES, instance=equipo)

        if formulario.is_valid():

            equipo = formulario.save(commit=False)
            equipo.save()

            return redirect(
                reverse('activos:equipos_lista')
            )

        contexto = {
            'form': formulario,
            'tag': self.tag,
            'operation': "Editar",
            'equipo_id': equipo.id,
            'imagen': self.obtener_UrlImagen(equipo.imagen)
        }
        return render(request, self.template_name, contexto)


class EquipoAPI(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by("-created_date")
    serializer_class = EquipoSerializer
    pagination_class = GenericPagination

    filter_backends = (DjangoFilterBackend,)
    filter_class = EquipoFilter


class EquipoTreeListView(View):

    def __init__(self):
        self.template_name = "equipo/arbol.html"

    def get(self, request, pk):

        equipo = get_object_or_404(Equipo, pk=pk)

        contexto = {
            "equipo": equipo
        }

        return render(request, self.template_name, contexto)


class EquipoTreeAPI(View):

    def get(self, request, pk):

        daddies = Equipo.objects.filter(pk=pk)

        serializador = EquipoTreeSerilizado()
        lista_json = serializador.get_Json(daddies)

        return HttpResponse(
            lista_json,
            content_type="application/json"
        )


class EquipoHistory(View):

    def __init__(self):
        self.template_name = 'equipo/historia.html'

    def get(self, request, pk):

        registros = Equipo.history.filter(id=pk).order_by("history_date")

        contexto = {
            'operation': "Historia",
            'equipo_id': pk,
            'registros': registros
        }

        return render(request, self.template_name, contexto)


# ----------------- EQUIPO - ANEXO ----------------- #

class AnexoTextoView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos/anexos_texto.html'

    def get(self, request, pk):
        id_equipo = pk
        anexos = AnexoTexto.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoTextoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        form = AnexoTextoForm(request.POST)
        anexos = AnexoTexto.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)

        if form.is_valid():
            texto = form.save(commit=False)
            texto.equipo_id = id_equipo
            texto.save()
            anexos = AnexoTexto.objects.filter(equipo=id_equipo)
            form = AnexoTextoForm()
        return render(request, 'equipo/anexos/anexos_texto.html',
                      {'form': form, 'id': id_equipo, 'anexos': anexos,
                       'equipo': equipo})


class AnexoImagenView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos/anexos_imagen.html'

    def get(self, request, pk):
        id_equipo = pk
        anexos = AnexoImagen.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoImagenForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        anexos = AnexoImagen.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoImagenForm(request.POST, request.FILES)

        if form.is_valid():

            imagen_anexo = AnexoImagen()
            imagen_anexo.descripcion = request.POST['descripcion']
            if 'ruta' in request.POST:
                imagen_anexo.ruta = request.POST['ruta']
            else:
                imagen_anexo.ruta = request.FILES['ruta']
            imagen_anexo.equipo_id = id_equipo
            imagen_anexo.save()
            form = AnexoImagenForm()
            anexos = AnexoImagen.objects.filter(equipo=id_equipo)
            # return render(request, self.template_name,
            #               {'form': form, 'id': id_equipo, 'anexos': anexos,
            #                'equipo': equipo})
        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }
        return render(request, self.template_name, contexto)


class AnexoArchivoView(View):

    def __init__(self):
        self.template_name = 'equipo/anexos/anexos_archivo.html'

    def get(self, request, pk):
        id_equipo = pk
        anexos = AnexoArchivo.objects.filter(equipo=id_equipo)
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)

    def post(self, request, pk):
        id_equipo = pk
        equipo = Equipo.objects.get(id=id_equipo)
        form = AnexoArchivoForm(request.POST, request.FILES)
        anexos = AnexoArchivo.objects.filter(equipo=id_equipo)

        if form.is_valid():
            archivo_anexo = AnexoArchivo()
            archivo_anexo.descripcion = request.POST['descripcion']
            if 'archivo' in request.POST:
                archivo_anexo.archivo = request.POST['archivo']
            else:
                archivo_anexo.archivo = request.FILES['archivo']
            archivo_anexo.equipo_id = id_equipo
            archivo_anexo.save()
            anexos = AnexoArchivo.objects.filter(equipo=id_equipo)
            form = AnexoArchivoForm()

        contexto = {
            'form': form,
            'id': id_equipo,
            'equipo': equipo,
            'anexos': anexos,
        }

        return render(request, self.template_name, contexto)


class AnexoTextoAPI(viewsets.ModelViewSet):
    queryset = AnexoTexto.objects.all()
    serializer_class = AnexoTextoSerializer
    pagination_class = GenericPagination


class AnexoArchivoAPI(viewsets.ModelViewSet):
    queryset = AnexoArchivo.objects.all()
    serializer_class = AnexoArchivoSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('equipo',)


class AnexoImagenAPI(viewsets.ModelViewSet):
    queryset = AnexoImagen.objects.all()
    serializer_class = AnexoImagenSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('equipo',)


# ----------------- UBICACION ----------------- #

class UbicacionListView(TemplateView):
    template_name = 'ubicacion/lista.html'


class UbicacionCreateView(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/formulario.html'
    success_url = reverse_lazy('activos:ubicaciones_lista')
    operation = "Nueva"

    def get_context_data(self, **kwargs):
        contexto = super(UbicacionCreateView, self).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/formulario.html'
    success_url = reverse_lazy('activos:ubicaciones_lista')
    operation = "Editar"

    def get_context_data(self, **kwargs):
        contexto = super(UbicacionUpdateView, self).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class UbicacionAPI(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('clave', 'descripcion',)


class UbicacionAPI2(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)


# ----------------- ODOMETRO ----------------- #

class OdometroListView(View):
    def __init__(self):
        self.template_name = 'odometro/lista.html'

    def get(self, request):

        formulario = OdometroFiltersForm()

        contexto = {
            'form': formulario
        }

        return render(request, self.template_name, contexto)

    def post(self, request):
        return render(request, self.template_name, {})


class OdometroCreateView(CreateView):
    model = Odometro
    form_class = OdometroForm
    template_name = 'odometro/formulario.html'
    success_url = reverse_lazy('activos:odometros_lista')
    operation = "Nuevo"

    def get_context_data(self, **kwargs):
        contexto = super(OdometroCreateView, self).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class OdometroUpdateView(UpdateView):
    model = Odometro
    form_class = OdometroForm
    template_name = 'odometro/formulario.html'
    success_url = reverse_lazy('activos:odometros_lista')
    operation = "Editar"

    def get_context_data(self, **kwargs):
        contexto = super(OdometroUpdateView, self).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class OdometroAPI(viewsets.ModelViewSet):
    queryset = Odometro.objects.all()
    serializer_class = OdometroSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = OdometroFilter


# ----------------- UDM ODOMETRO ----------------- #

class UdmOdometroListView(TemplateView):
    template_name = 'udm_odometro/lista.html'


class UdmOdometroCreateView(CreateView):
    model = UdmOdometro
    form_class = UdmOdometroForm
    template_name = 'udm_odometro/formulario.html'
    success_url = reverse_lazy('activos:udms_odometro_lista')
    operation = "Nueva"

    def get_context_data(self, **kwargs):
        contexto = super(
            UdmOdometroCreateView,
            self
        ).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class UdmOdometroUpdateView(UpdateView):
    model = UdmOdometro
    form_class = UdmOdometroForm
    template_name = 'udm_odometro/formulario.html'
    success_url = reverse_lazy('activos:udms_odometro_lista')
    operation = "Editar"

    def get_context_data(self, **kwargs):
        contexto = super(
            UdmOdometroUpdateView,
            self
        ).get_context_data(**kwargs)
        contexto['operation'] = self.operation
        return contexto


class UdmOdometroAPI(viewsets.ModelViewSet):
    queryset = UdmOdometro.objects.all()
    serializer_class = UdmOdometroSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('clave', 'descripcion',)


class UdmOdometroAPI2(viewsets.ModelViewSet):
    queryset = UdmOdometro.objects.all()
    serializer_class = UdmOdometroSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)


# ----------------- MEDICION ----------------- #


class MedicionOdometroView(View):

    def __init__(self):
        self.template_name = 'medicion/lista.html'

    def get(self, request, pk):
        formulario_medicion = MedicionForm()
        id_odometro = pk
        odometro = Odometro.objects.get(id=id_odometro)
        formulario = MedicionFiltersForm()

        contexto = {
            'formulario_medicion': formulario_medicion,
            'form': formulario,
            'id_odometro': id_odometro,
            'odometro': odometro,
        }

        return render(request, self.template_name, contexto)


class MedicionAPI(viewsets.ModelViewSet):
    queryset = Medicion.objects.all().order_by('-fecha')
    serializer_class = MedicionSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = MedicionFilter
