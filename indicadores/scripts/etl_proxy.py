# coding: utf8
import argparse
import time, datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, Unicode, Date, Time, ForeignKey, create_engine
from urlparse import urlparse

from pprint import pprint


parser = argparse.ArgumentParser(description='Load proxy log to RDB.')
parser.add_argument('--init', choices=['true','false'], default='false', help="create database and tables, default: false")
parser.add_argument('--db_url', default='sqlite:///proxy.sqlite', help="DB URL, default: sqlite:///proxy.sqlite")
parser.add_argument('--log', type=argparse.FileType('r'), required=True, help='proxy access log file')

args = parser.parse_args()


##################
# DataBase Model #
##################
Base = declarative_base()
class Request(Base):
    __tablename__ = 'requests'
    id            = Column(Integer, primary_key=True)

    date          = Column(Date)
    time          = Column(Time)

    url_scheme    = Column(Unicode)
    url_file_type = Column(Unicode)
    url_port      = Column(Integer)
    
    method        = Column(Unicode)
    result        = Column(Integer)

    comment       = Column(Unicode)

    client_id     = Column(Integer, ForeignKey('clients.id'))
    server_id     = Column(Integer, ForeignKey('servers.id'))    

    

class Client(Base):
    __tablename__ = 'clients'
    id            = Column(Integer, primary_key=True)
    addr          = Column(Unicode)
    requests      = relationship("Request", backref="client")
    
class Server(Base):
    __tablename__ = 'servers'
    id            = Column(Integer, primary_key=True)
    addr          = Column(Unicode)
    requests      = relationship("Request", backref="server")
    tld           = Column(Unicode)



    
####################
# database connect #
####################
engine     = create_engine(args.db_url)
Session = sessionmaker(bind=engine)


if args.init == 'true':
    Base.metadata.create_all(engine)


session = Session()

##################
# Parse log file #
##################
for l in args.log.readlines():
    try:
        fields = l.decode('utf-8').split(' ')
    except:
        continue
    
    day  = datetime.date(*time.strptime( fields[0], "%Y.%m.%d" )[:3])
    hour = datetime.time(*time.strptime( fields[1], "%H:%M:%S" )[3:6])
    client_addr = fields[3]

    # parse url
    url    = urlparse(fields[4])

    url_scheme = url.scheme
    url_netloc = url.netloc
    url_file_type   = url.path.split('/')[-1].split('.')[-1]
    url_port   = url.port
    if not url_port:
        url_port = 80
    
        
    if fields[5] == "*DENIED*":
        if fields[6] == u"Extensión" and fields[7] == "bloqueada:":
            method = fields[9]
            result = fields[15]
            comment = u" ".join(fields[6:9])
        elif fields[6] == 'URL' and fields[7] == "bloqueada":
            method = fields[12]
            result = fields[20]
            comment = u" ".join(fields[6:11]) + url.path
        elif fields[9] == 'Bloqueo' and fields[10] == 'general':
            method = fields[27]
            result = fields[32]
            comment = u" ".join(fields[6:26])
        else:
            method = fields[10]
            result = fields[16]
            comment = u" ".join(fields[6:10])
    elif fields[5] == "*EXCEPTION*":
        if fields[6] == u"Dirección" and fields[7] == "IP":
            method =  fields[16]
            result = fields[21]
            comment = u" ".join(fields[6:16])
        elif fields[6] == "Sitio" and fields[7] == "presente":
            method = fields[13]
            result = fields[18]
            comment = u" ".join(fields[6:13]) 
    else:
        result = fields[11]
        method = fields[6]
        comment = u""


    ######################
    # Upsert to database #
    ######################        
    request = Request( date          = day,
                       time          = hour,
                       url_scheme    = url_scheme,
                       url_file_type = url_file_type,
                       url_port      = url_port,
                       method        = method,
                       result        = result,
                       comment       = comment )

        
    server = session.query(Server).filter(Server.addr == url_netloc).first()
    if not(server):
        server = Server(addr = url_netloc)
        session.add(server)
    server.requests.append( request )

    client = session.query(Client).filter(Client.addr == client_addr).first()
    if not(client):
        client = Client(addr = client_addr)
        session.add(client)
    client.requests.append( request )

    
    session.commit()
