# pypy

> A Python nyelv gyors és kompatibilis alternatív implementációja. További információ: <https://doc.pypy.org>.

- REPL (interaktív shell) indítása:

`pypy`

- Egy adott Python fájlban lévő szkript végrehajtása:

`pypy {{path/to/file.py}}`

- Szkript végrehajtása egy interaktív shell részeként:

`pypy -i {{path/to/file.py}}`

- Python kifejezés végrehajtása:

`pypy -c "{{expression}}"`

- Könyvtári modul futtatása szkriptként (az opciós lista lezárása):

`pypy -m {{module}} {{arguments}}`

- Csomag telepítése pip segítségével:

`pypy -m pip install {{package_name}}`

- Interaktív hibakeresés egy Python szkriptben:

`pypy -m pdb {{path/to/file.py}}`
