import argparse
from Bio import Medline
import time, datetime
from itertools import combinations
import networkx as nx
from networkx.readwrite import json_graph
import json
import sys

from pprint import pprint


parser = argparse.ArgumentParser(description='create a meshterm network from a medline file')
parser.add_argument('medline', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help="citations file in medline format")
parser.add_argument('json_out', type=argparse.FileType('w'), nargs='?', default=sys.stdout, help='JSON output')
args    = parser.parse_args()

records = Medline.parse( args.medline )

g = nx.Graph()

for r in records:
    
    # evenly format dates
    if 'CRDT' in r.keys():
        conv = time.strptime( r['CRDT'][0], "%Y/%m/%d %H:%M" )
        r['CRDT'] = datetime.datetime(*conv[:6]) # date created
    if 'DCOM' in r.keys():
        conv = time.strptime( r['DCOM'], "%Y%m%d" )
        r['DCOM'] = datetime.datetime(*conv[:6]) # date completed
    if 'LR' in r.keys():
        conv = time.strptime( r['LR'], "%Y%m%d" )
        r['LR'] = datetime.datetime(*conv[:6]) # date revised
    if 'DEP' in r.keys():
        conv = time.strptime( r['DEP'], "%Y%m%d" )
        r['DEP'] = datetime.datetime(*conv[:6]) # date of electronic publication

    # let PubMed handle keys
    r['_id'] = int(r['PMID'])

    if 'MH' in r:
        for edge in combinations(r['MH'], 2):
            if g.get_edge_data(*edge):
                w = g.get_edge_data(*edge)['w'] + 1
            else:
                w =1
            g.add_edge(*edge, w=w)


h = nx.Graph()

for e in g.edges():
    if g.get_edge_data(*e)['w']>4:
	h.add_edge(*e)

data = json_graph.node_link_data(h)
s = json.dumps(data)
args.json_out.write(s)
