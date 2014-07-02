# coding: utf-8

from elixir import *
import time, datetime
import csv
import argparse
import pprint

parser = argparse.ArgumentParser(description='Extrae unos datos de los XMLs, los deja en un diccionario.')
parser.add_argument('--db_url', required=True)
parser.add_argument('--color', dest='color', action='store_true')
parser.add_argument('--no_color', dest='color', action='store_false')
parser.add_argument('--impresoras', type=argparse.FileType('r'), required=True, help='Relación de impresoras en formato CSV')
parser.add_argument('--volumen', type=argparse.FileType('r'), required=True, help='Volumen de impresión en formato CSV')
parser.set_defaults(color=False)
args = parser.parse_args()

# sqlite:///cfe.sqlite
metadata.bind = args.db_url
# metadata.bind.echo = True

class Volumen(Entity):
    fecha     = Field(Date)
    volumen   = Field(Integer)
    impresora = ManyToOne('Impresora')
    color     = Field(Boolean)

    using_options(tablename="impresoras_volumen")


class Impresora(Entity):
    serie  = Field(Unicode(128), primary_key=True )
    modelo = Field(Unicode(128))
    ubicacion = Field(Unicode(128))
    volumenes = OneToMany('Volumen')
    using_options(tablename="impresoras")



setup_all()
create_all()


# carga relación de impresoras
impresoras_reader = csv.reader(args.impresoras, delimiter=',', quotechar='"')
encabezado = impresoras_reader.next()
for row in impresoras_reader:
    #No., IMPRESORA , MODELO, N/S, Dirección MAC, IP, Ubicación Actual
    if not Impresora.get_by(serie=row[3]):
        Impresora( serie = row[3],
                   modelo = row[2],
                   ubicacion = u"%s" % row[6] )
        session.commit()



# carga volumenes de impresión por impresora
volumen_reader = csv.reader(args.volumen, delimiter=';', quotechar='"')

encabezado = volumen_reader.next()
months     = ['ENE','FEB','MZO','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']

for row in volumen_reader:
    impresora = Impresora.get_by(serie=row[1])

    if not impresora:
        impresora = Impresora( serie = row[1],
                               modelo = 'Modelo Desconocido',
                               ubicacion = u"Ubicación Desconocida" )
        session.commit()


    for n in range(2,len(row)):
        volumen = row[n]
        if volumen == '':
            volumen = 0
        else:
            volumen = int(volumen)

        (mes, anyo) = encabezado[n].split('-')
        anyo = int(anyo)+2000
        mes  = months.index(mes)+1
        fecha = datetime.date(anyo,mes,28)

        Volumen( fecha   = fecha,
                 volumen = volumen,
                 impresora = impresora,
                 color = args.color)
        session.commit()
