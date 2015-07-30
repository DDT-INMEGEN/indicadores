# coding: utf8
import argparse
import time, datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey, create_engine
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
    client_id     = Column(Integer, ForeignKey('clients.id'))
    
    url_scheme    = Column(String)
    server_id     = Column(Integer, ForeignKey('servers.id'))
    url_file_type = Column(String)
    url_port      = Column(Integer)
    
    method        = Column(String)
    result        = Column(Integer)

    comment       = Column(String)


class Client(Base):
    __tablename__ = 'clients'
    id            = Column(Integer, primary_key=True)
    addr          = Column(String)
    requests      = relationship("Request", backref="client")
    
class Server(Base):
    __tablename__ = 'servers'
    id            = Column(Integer, primary_key=True)
    addr          = Column(String)
    requests      = relationship("Request", backref="server")




    
####################
# database connect #
####################
engine     = create_engine(args.db_url)
Session = sessionmaker(bind=engine)


if args.init == 'true':
    Base.metadata.create_all(engine)





#################
# Read log file #
#################
for l in args.log.readlines():
    fields = l.split(' ')
    
    day  = datetime.date(*time.strptime( fields[0], "%Y.%m.%d" )[:3])
    hour = datetime.time(*time.strptime( fields[1], "%H:%M:%S" )[3:6])
    client = fields[3]

    # parse url
    url    = urlparse(fields[4])

    url_scheme = url.scheme
    url_netloc = url.netloc
    url_file_type   = url.path.split('/')[-1].split('.')[-1]
    url_port   = url.port
    if not url_port:
        url_port = 80
    
        
    if fields[5] == "*DENIED*":
        if fields[6] == "Extensión" and fields[7] == "bloqueada:":
            method = fields[9]
            result = fields[15]
            comment = " ".join(fields[6:9])
        elif fields[6] == 'URL' and fields[7] == "bloqueada":
            method = fields[12]
            result = fields[20]
            comment = " ".join(fields[6:11]) + url.path
        elif fields[9] == 'Bloqueo' and fields[10] == 'general':
            method = fields[27]
            result = fields[32]
            comment = " ".join(fields[6:26])
        else:
            method = fields[10]
            result = fields[16]
            comment = " ".join(fields[6:10])
    elif fields[5] == "*EXCEPTION*":
        if fields[6] == "Dirección" and fields[7] == "IP":
            method =  fields[16]
            result = fields[21]
            comment = " ".join(fields[6:16])
        elif fields[6] == "Sitio" and fields[7] == "presente":
            method = fields[13]
            result = fields[18]
            comment = " ".join(fields[6:13]) 
    else:
        result = fields[11]
        method = fields[6]
        comment = ""

    #print day,hour,method,result
