# python

> Python nyelvi értelmező. További információ: <https://www.python.org>.

- REPL (interaktív shell) indítása:

`python`

- Egy adott Python fájl végrehajtása:

`python {{path/to/file.py}}`

- Egy adott Python fájl végrehajtása és egy REPL indítása:

`python -i {{path/to/file.py}}`

- Egy Python-kifejezés végrehajtása:

`python -c "{{expression}}"`

- A megadott könyvtári modul szkriptjének futtatása:

`python -m {{module}} {{arguments}}`

- Egy csomag telepítése a `pip` segítségével:

`python -m {{pip}} install {{package_name}}`

- Egy Python szkript interaktív hibakeresése:

`python -m {{pdb}} {{path/to/file.py}}`

- A beépített HTTP-kiszolgáló elindítása a 8000-es porton az aktuális könyvtárban:

`python -m {{http.server}}`
