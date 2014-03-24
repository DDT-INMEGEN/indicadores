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
rows = htsql.produce("/hesk_tickets{custom4,custom1, name, custom3, subject, priority}")



#  +-----------------+---------------------+---------------------------+-------------+--------------------------------+----------+
#  | custom4         | custom1             | name                      | custom3     | subject                        | priority |
#  +-----------------+---------------------+---------------------------+-------------+--------------------------------+----------+


partitions = AutoVivification()

for row in rows:
    partitions[row.custom4][row.custom1][row.name][row.custom3][row.subject] = row.priority


tipos = []
for tipo in partitions:
    children = []
    for ubicacion in partitions[tipo]:
        subchildren = []
        for name in partitions[tipo][ubicacion]:
            subsubchildren = []
            for subtipo in partitions[tipo][ubicacion][name]:
                subsubsubchildren = []
                for subject in partitions[tipo][ubicacion][name][subtipo]:
                    subsubsubchildren.append( {'name': subject,
                                               'size': 10 * (int(partitions[tipo][ubicacion][name][subtipo][subject]) + 1)  } )
                subsubchildren.append( {'name': subtipo,
                                        'children': subsubsubchildren } )
            subchildren.append( {'name': name,
                                 'children': subsubchildren } )
        children.append( {'name': ubicacion,
                          'children': subchildren } )
    tipos.append( {'name': tipo,
                   'children': children } )


tickets = {'name': 'tickets',
           'children': tipos }




import json
f = open('tickets.json', 'w')
f.write(json.dumps(tickets, indent=4))
f.close()


