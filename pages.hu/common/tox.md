# tox

> Automatizálja a Python tesztelését több Python verzióban. Használja a tox.ini-t a környezetek és a tesztparancs konfigurálásához. További információ: <https://github.com/tox-dev/tox>.

- Tesztek futtatása az összes tesztkörnyezetben:

`tox`

- Hozzon létre egy `tox.ini` konfigurációt:

`tox-quickstart`

- Az elérhető környezetek listázása:

`tox --listenvs-all`

- Tesztek futtatása egy adott környezetben (pl. python 3.6):

`tox -e {{py36}}`

- A virtuális környezet újbóli létrehozásának kikényszerítése:

`tox --recreate -e {{py27}}`
