# coding: utf-8

import xmltodict
import argparse

parser = argparse.ArgumentParser(description='Extrae unos datos de los XMLs, los deja en un diccionario.')
parser.add_argument('xmlfiles', type=file, nargs='+', help='uno o más archivos XML de la CFE')

args = parser.parse_args()


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

    print ",".join([doc[comprobante]['@fecha'],
                    doc[comprobante]['@total'],])
#                    doc[comprobante]['@subTotal'],
#                    doc[comprobante][conceptos][concepto]['@cantidad']])
