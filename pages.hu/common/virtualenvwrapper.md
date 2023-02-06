# virtualenvwrapper

> Egyszerű csomagoló parancsok csoportja a Python `virtualenv` eszközéhez. További információ: <http://virtualenvwrapper.readthedocs.org>.

- Új Python `virtualenv` létrehozása a `$WORKON_HOME` oldalon:

`mkvirtualenv {{virtualenv_name}}`

- Hozzon létre egy `virtualenv` egy adott Python-verzióhoz:

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- Aktiváljon vagy használjon egy másik `virtualenv`:

`workon {{virtualenv_name}}`

- A `virtualenv` leállítása :

`deactivate`

- Az összes virtuális környezet listázása:

`lsvirtualenv`

- A `virtualenv` eltávolítása:

`rmvirtualenv {{virtualenv_name}}`

- Az összes virtualenvwrapper parancs összefoglalása:

`virtualenvwrapper`
