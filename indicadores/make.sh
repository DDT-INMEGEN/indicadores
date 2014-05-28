#!/bin/bash

echo "Activating environment"
source ~/indicadores_env/bin/activate

echo "Generating tg_sunburst.json"
python scripts/tg_sunburst.py

echo "Generating static html"
python scripts/make_site.py
