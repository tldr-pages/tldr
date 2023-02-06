# git tag

> Címkék létrehozása, listázása, törlése vagy ellenőrzése. A címke egy statikus hivatkozás egy adott commitra. További információ: <https://git-scm.com/docs/git-tag>.

- Az összes címke listázása:

`git tag`

- Létrehoz egy címkét a megadott névvel, amely az aktuális commitra mutat:

`git tag {{tag_name}}`

- Adott nevű címke létrehozása egy adott commitra mutatva:

`git tag {{tag_name}} {{commit}}`

- Létrehoz egy megjegyzésekkel ellátott címkét a megadott üzenettel:

`git tag {{tag_name}} -m {{tag_message}}`

- A megadott nevű tag törlése:

`git tag -d {{tag_name}}`

- Frissített címkék lekérése az upstreamből:

`git fetch --tags`

- Az összes olyan címke listázása, amelynek ősei tartalmazzák az adott commitot:

`git tag --contains {{commit}}`
