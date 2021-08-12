# virtualenvwrapper

> Grup de comenzi simple de împachetare pentru instrumentul `virtualenv` al lui Python.
> Mai multe informaţii: <http://virtualenvwrapper.readthedocs.org>

- Creați un nou Python `virtualenv` în `$WORKON_HOME`:

`mkvirtualenv {{virtualenv_name}}`

- Creați un `virtualenv` pentru o anumită versiune Python:

`mkvirtualenv --python {{/usr/local/bin/python3.8}} {{virtualenv_name}}`

- Activați sau utilizați un alt `virtualenv`:

`workon {{virtualenv_name}}`

- Opriţi `virtualenv`:

`deactivate`

- Listează toate mediile virtuale:

`lsvirtualenv`

- Elimină un `virtualenv`:

`rmvirtualenv {{virtualenv_name}}`

- Obține rezumatul tuturor comenzilor virtualenvwrapper:

`virtualenvwrapper`
