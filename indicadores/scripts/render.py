import argparse
import sys, os
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(description="Render html into a jinja2 template")
parser.add_argument('--template', required=True, type=argparse.FileType('r'),
                    help='path to jinja2 template')
parser.add_argument('--html', required=True, type=argparse.FileType('r'),
                    help='path to html to be rendered into template')
parser.add_argument('--outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                    help='path to output, default to stdout')


if __name__ == '__main__':
    args     = parser.parse_args()
    template = args.template
    html     = args.html.read()
    outfile  = args.outfile

    t = Environment(
        loader=FileSystemLoader(
            os.path.dirname(
                os.path.realpath( template.name )))).get_template( os.path.split(template.name)[1] )


    with outfile as f:
        f.write( t.render( html=html ) )
