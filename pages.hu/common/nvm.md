# nvm

> Telepítés, eltávolítás vagy váltás a Node.js verziók között. Támogatja az olyan verziószámokat, mint "12.8" vagy "v16.13.1", és az olyan címkéket, mint "stable", "system", stb. További információk: <https://github.com/creationix/nvm>.

- A Node.js egy adott verziójának telepítése:

`nvm install {{node_version}}`

- A Node.js egy adott verziójának használata az aktuális héjban:

`nvm use {{node_version}}`

- A Node.js alapértelmezett verziójának beállítása:

`nvm alias default {{node_version}}`

- Az összes elérhető Node.js verzió listázása és az alapértelmezett verzió kiemelése:

`nvm list`

- Egy adott Node.js verzió eltávolítása:

`nvm uninstall {{node_version}}`

- A Node.js egy adott verziójának REPL-jének elindítása:

`nvm run {{node_version}} --version`

- Egy szkript végrehajtása a Node.js egy adott verziójában:

`nvm exec {{node_version}} node {{app.js}}`
