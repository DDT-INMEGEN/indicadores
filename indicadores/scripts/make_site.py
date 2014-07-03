from jinja2 import Environment, FileSystemLoader
import os,sys

reload(sys)
sys.setdefaultencoding('utf-8')

reportes = [
    { 'reporte': 'rspi_coautores.html', 'template': 'dashboard_investigacion_d3.html' },
    { 'reporte': 'rspi_mesh.html', 'template': 'dashboard_investigacion_d3.html' },
    { 'reporte': 'rspi_colaboradores.html', 'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_recursos_destino.html', 'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_recursos_origen.html', 'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_status.html',  'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_investigadores.html',  'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_proyectos_costos_sunburst.html',  'template': 'dashboard_investigacion_d3.html' },
#    { 'reporte': 'rspi_proyectos_convenio.html',  'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_usuarios_puesto.html',  'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_usuarios_area.html',  'template': 'dashboard_investigacion.html' },
    { 'reporte': 'rspi_tesis_avance.html',  'template': 'dashboard_investigacion.html' },

    { 'reporte': "tg_categorias.html", 'template': 'dashboard_tg.html' },
    { 'reporte': "tg_estados.html", 'template': 'dashboard_tg.html' },
    { 'reporte': "tg_internos_externos.html", 'template': 'dashboard_tg.html' },
    { 'reporte': "tg_tiempo.html", 'template': 'dashboard_tg.html' },
    { 'reporte': "tg_sunburst.html", 'template': 'dashboard_tg_d3.html' },


    { 'reporte': 'ti_tipos.html',  'template': 'dashboard_ti.html' },
    { 'reporte': 'ti_personas.html',  'template': 'dashboard_ti.html' },
    { 'reporte': 'ti_dinamica.html',  'template': 'dashboard_ti.html' },

    { 'reporte': 'admin_cfe.html',  'template': 'dashboard_admin.html' },
    { 'reporte': 'admin_impresoras_dinamica.html',  'template': 'dashboard_admin.html' },
]


for r in reportes:
    html     = open('src/'+r['reporte'] ).read()
    template = open('templates/'+r['template'], 'r')
    outfile  = open('static/'+r['reporte'], 'w')

    t = Environment(
        loader=FileSystemLoader(
            os.path.dirname(
                os.path.realpath( template.name )))).get_template( os.path.split(template.name)[1] )

    with outfile as f:
        f.write( t.render( html=html ) )
