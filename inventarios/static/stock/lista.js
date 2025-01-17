/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

var url_grid = window.location.origin + "/api/stock/"
var targeta_filtros = null
var targeta_resultados = null
var modal= null

/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    targeta_filtros = new TargetaFiltros()
    targeta_resultados = new TargetaResultados()
})

// Asigna eventos a teclas
$(document).keypress(function (e) {

    // Tecla Enter
    if (e.which == 13) {

        targeta_resultados.grid.buscar()
    }
})


/*-----------------------------------------------*\
            OBJETO: Targeta Filtros
\*-----------------------------------------------*/

function TargetaFiltros() {

    this.$id = $('#id_panel')

    this.$articulo = $('#id_articulo') 
    this.$almacen = $('#id_almacen') 
    this.$cantidad_mayorque = $('#id_cantidad_mayorque')
    this.$cantidad_menorque = $('#i_cantidad_menorque')

    this.$boton_buscar =  $('#boton_buscar')
    this.$boton_limpiar =  $('#boton_limpiar')

    this.init()
}
TargetaFiltros.prototype.init = function () {

    pagina.activar_Arbol("tree_inventarios")

    if (this.$articulo.val() != "") {
        alertify.notify("Existencias del articulo: " + this.$articulo.find(":selected").text())
        pagina.activar_Opcion("opt_articulos")
    }

    if (this.$almacen.val() != "") {
        alertify.notify("Existencias en el almacen: " + this.$almacen.find(":selected").text())
        pagina.activar_Opcion("opt_almacenes")
    }    

    this.$articulo.select2()
    this.$almacen.select2()

    this.$id.addClass('collapsed-box')

    this.$boton_buscar.on("click", this, this.click_BotonBuscar)
    this.$boton_limpiar.on("click", this, this.click_BotonLimpiar)
}
TargetaFiltros.prototype.get_Filtros = function (_page, _pageSize) {

    return {
        page: _page,
        pageSize: _pageSize,

        articulo: this.$articulo.val(),
        almacen: this.$almacen.val(),
        cantidad_mayorque: this.$cantidad_mayorque.val(),
        cantidad_menorque: this.$cantidad_menorque.val(),
        
    }
}
TargetaFiltros.prototype.click_BotonBuscar = function(e) {

    e.preventDefault()
    targeta_resultados.grid.buscar()
    
}
TargetaFiltros.prototype.click_BotonLimpiar = function (e) {

    e.preventDefault()
    e.data.$articulo.val("").trigger('change')
    e.data.$almacen.val("").trigger('change')
    e.data.$cantidad_mayorque.val("")
    e.data.$cantidad_menorque.val("")   
}

/*-----------------------------------------------*\
            OBJETO: RESULTADOS
\*-----------------------------------------------*/

function TargetaResultados() {

    this.toolbar = new Toolbar()
    this.grid = new GridPrincipal()
}


/*-----------------------------------------------*\
            OBJETO: GRID
\*-----------------------------------------------*/

function GridPrincipal() {

    this.$id = $("#grid_principal")
    this.kfuente_datos = null
    this.kgrid = null

    this.init()
}
GridPrincipal.prototype.init = function () {

    kendo.culture("es-MX")

    this.kfuente_datos = new kendo.data.DataSource(this.get_FuenteDatosConfig())

    this.kgrid = this.$id.kendoGrid(this.get_Config())
}
GridPrincipal.prototype.get_Config = function () {

    return {
        dataSource: this.kfuente_datos,
        columnMenu: false,
        groupable: false,
        sortable: false,
        editable: false,
        resizable: true,
        selectable: true,
        scrollable: false,
        columns: this.get_Columnas(),
        scrollable: true,
        pageable: true,
        noRecords: {
            template: "<div class='grid-empy'> No se encontraron registros </div>"
        },
    }
}
GridPrincipal.prototype.get_Campos = function (e) {

    return {
        almacen: { type: "string" },
        articulo: { type: "string" },
        cantidad: { type: "string"},
        udm: { type: "string"},
    }
}
GridPrincipal.prototype.get_Columnas = function (e) {

    return [
        { field: "almacen" , title: "Almacen", width: "120px" },
        { field: "articulo" , title: "Articulo", width: "120px" },
        { field: "cantidad" , title: "Cantidad", width: "120px" },
        { field: "udm" , title: "UDM", width: "120px" },
    ]
}
GridPrincipal.prototype.get_FuenteDatosConfig = function (e) {

    return {

        serverPaging: true,
        pageSize: 10,
        transport: {
            read: {

                url: url_grid,
                type: "GET",
                dataType: "json",
                cache: false

            },
            parameterMap: function (data, action) {
                if (action === "read") {

                    return targeta_filtros.get_Filtros(data.page, data.pageSize)
                }
            }
        },
        schema: {
            data: "results",
            total: "count",
            model: {
                fields: this.get_Campos()
            }
        },
        error: function (e) {
            alert("Status: " + e.status + "; Error message: " + e.errorThrown)
        },
    }
}
GridPrincipal.prototype.buscar =  function() {
    this.kfuente_datos.page(1)
}

/*-----------------------------------------------*\
            OBJETO: TOOLBAR
\*-----------------------------------------------*/

function Toolbar() {

    this.$boton_exportar = $("#boton_exportar")

    this.init()
}
Toolbar.prototype.init = function (e) {

    this.$boton_exportar.on("click", this, this.click_BotonExportar)
}
Toolbar.prototype.click_BotonExportar = function(e) {
    e.preventDefault()
    return null
}