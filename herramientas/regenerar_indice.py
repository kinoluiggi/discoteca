#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
regenerar_indice.py
Reconstruye indice.json desde los fragmentos de álbum (albums/**/*.json),
aplicando las bajas de eliminados.json. Pensado para correr automático
en GitHub Actions, pero también sirve localmente:

    python3 herramientas/regenerar_indice.py
"""

import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
    if '__file__' in dir() else '.'
if len(sys.argv) > 1:
    RAIZ = os.path.expanduser(sys.argv[1])

# localizar carpeta albums (raíz o dentro de discoteca/)
CARPETA = None
PREFIJO = ''
for cand, pref in (('albums', ''), ('discoteca/albums', 'discoteca/')):
    if os.path.isdir(os.path.join(RAIZ, cand)):
        CARPETA = os.path.join(RAIZ, cand)
        PREFIJO = pref
        break
if not CARPETA:
    print('✗ No encuentro la carpeta albums')
    sys.exit(1)

# bajas
eliminados = set()
ruta_elim = os.path.join(RAIZ, PREFIJO + 'eliminados.json')
if os.path.exists(ruta_elim):
    try:
        with open(ruta_elim, encoding='utf-8') as f:
            eliminados = set(json.load(f))
    except Exception:
        pass

indice = []
leidos = errores = 0
for raiz, _, archivos in os.walk(CARPETA):
    for nombre in sorted(archivos):
        if not nombre.endswith('.json'):
            continue
        ruta = os.path.join(raiz, nombre)
        try:
            with open(ruta, encoding='utf-8') as f:
                a = json.load(f)
        except Exception:
            errores += 1
            continue
        leidos += 1
        if a.get('id') in eliminados:
            continue
        rel = os.path.relpath(ruta, os.path.join(RAIZ, PREFIJO)) \
            .replace(os.sep, '/')
        tracks = a.get('tracks', [])
        n_fuente = sum(1 for t in tracks
                       if t.get('videoId') or t.get('audio')
                       or t.get('soundcloud'))
        e = {
            'id': a.get('id'),
            'a': a.get('artista'),
            't': a.get('album'),
            'y': a.get('año'),
            'p': a.get('portada'),
            'n': len(tracks),
            'v': n_fuente,
            'r': rel,
        }
        if a.get('generos'):
            e['g'] = a['generos']
        if a.get('pais'):
            e['c'] = a['pais']
        indice.append(e)

indice.sort(key=lambda e: ((e['a'] or '').lower(),
                           e['y'] or 0,
                           (e['t'] or '').lower()))

salida = os.path.join(RAIZ, PREFIJO + 'indice.json')
with open(salida, 'w', encoding='utf-8') as f:
    json.dump(indice, f, ensure_ascii=False)

print(f'✓ {leidos} fragmentos leídos ({errores} ilegibles)')
print(f'✓ {len(eliminados)} bajas aplicadas')
print(f'✓ indice.json: {len(indice)} álbumes, '
      f'{os.path.getsize(salida)/1e6:.1f} MB')
