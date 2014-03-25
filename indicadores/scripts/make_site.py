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
