from urllib2 import Request, urlopen,URLError
import json
from pprint import pprint
from Bio import Entrez

# get list of author IDs from API
author_ids = []
try:
    req = Request('http://api.intranet.inmegen.gob.mx/api/protocolos/v1/autoresinternos/?format=json')
    res = urlopen(req)
    j = json.loads(res.read())
    for author in j['objects']:
        author_ids.append(author['id'])
except URLError, e:
    print "aguas", e


# get list of titles using author IDs
titles = set()
for Id in author_ids:
    try:
        req = Request("http://api.intranet.inmegen.gob.mx/api/protocolos/v1/publicacionlistinet/?format=json&autor=%s" % Id)
        res = urlopen(req)
        j = json.loads(res.read())
        for article in j['objects']:
            titles.add(article['titulo'])
    except URLError, e:
        print "aguas", e


# get pubmed entries using titles
for title in titles:
    h = Entrez.esearch(db="pubmed",
                       term=title,
                       field='title')
    r = Entrez.read(h)
    for Id in r['IdList']:
        h2 = Entrez.efetch(db="pubmed", id=Id, rettype="medline", retmode="text")
        print h2.read()
