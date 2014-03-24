class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
        return value
 

from htsql import HTSQL
import pprint

htsql = HTSQL("mysql://ddt:ttd@localhost/hesk")
rows = htsql.produce("/protocolos_gasto{proyecto{status, linea_de_investigacion{linea_investigacion_desc :as desc} :as linea, titulo}, descripcion, monto}")

# | proyecto                                                                            |                                  |            |
# +---------------+----------------------------------+----------------------------------+                                  |            |
# |               | linea                            |                                  |                                  |            |
# |               +----------------------------------+                                  |                                  |            |
# | status        | linea_investigacion_desc         | titulo                           | descripcion                      | monto      |


partitions = AutoVivification()

status = linea = titulo = concepto = ''
for row in rows:
    if row.proyecto.linea:
        linea = row.proyecto.linea.desc
    else:
        linea = 'misc'

    partitions[row.proyecto.status][linea][row.proyecto.titulo][row.descripcion] = row.monto



stati = []
for status in partitions:
    children = []
    for linea in partitions[status]:
        subchildren = []
        for clave in partitions[status][linea]:
            subsubchildren = []
            for concepto in partitions[status][linea][clave]:
                subsubchildren.append( {'name': concepto,
                                        'size': float(partitions[status][linea][clave][concepto])} )
            subchildren.append( {'name': clave,
                                 'children': subsubchildren } )
        children.append( {'name': linea,
                          'children': subchildren} )
    stati.append( {'name': status,
                 'children': children} )
    
proyectos = {'name': 'proyectos',
             'children': stati }


import json
f = open('proyectos.json', 'w')
f.write(json.dumps(proyectos, indent=4))
f.close()
