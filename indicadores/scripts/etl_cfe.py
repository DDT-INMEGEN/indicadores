# coding: utf-8

from elixir import *
import time, datetime
import xmltodict
import argparse


parser = argparse.ArgumentParser(description='Extrae unos datos de los XMLs, los deja en un diccionario.')
parser.add_argument('--db_url', required=True)
parser.add_argument('xmlfiles', type=file, nargs='+', help='uno o más archivos XML de la CFE')

args = parser.parse_args()

# sqlite:///cfe.sqlite
metadata.bind = args.db_url
# metadata.bind.echo = True

class Recibo(Entity):
    fecha = Field(Date)
    total = Field(Integer)
    kwh   = Field(Integer)

    using_options(tablename="recibos_cfe")


setup_all()
create_all()


for f in args.xmlfiles:
    doc = xmltodict.parse(f.read())
    if 'Comprobante' in doc.keys():
        comprobante = 'Comprobante'
        conceptos   = 'Conceptos'
        concepto    = 'Concepto'

    if 'cfdi:Comprobante' in doc.keys():
        comprobante = 'cfdi:Comprobante'
        conceptos   = 'cfdi:Conceptos'
        concepto    = 'cfdi:Concepto'
        
    #2012-07-03T18:12:20
    conv  = time.strptime(doc[comprobante]['@fecha'], "%Y-%m-%dT%H:%M:%S" )
    fecha = datetime.datetime(*conv[:6])

    Recibo(fecha = fecha,
           total = doc[comprobante]['@total'],
           kwh   = doc[comprobante][conceptos][concepto]['@cantidad'])
    
    session.commit()
                  



