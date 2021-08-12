# tox

> Automatizați testarea Python în mai multe versiuni Python.
> Utilizați tox.ini pentru a configura mediile și comanda de testare.
> Mai multe informaţii: <https://github.com/tox-dev/tox>

- Rulați teste pe toate mediile de testare:

`tox`

- Creați o configurație `tox.ini”:

`tox-quickstart`

- Listează mediile disponibile:

`tox --listenvs-all`

- Executați teste pe un mediu specific (de exemplu, piton 3.6):

`tox -e {{py36}}`

- Forțați mediul virtual să fie recreat:

`tox --recreate -e {{py27}}`
