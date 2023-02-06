# nvm

> Telepítés, eltávolítás vagy váltás a Node.js verziók között. Támogatja az olyan verziószámokat, mint a "12.8" vagy a "v16.13.1", és az olyan címkéket, mint a "stable", "system" stb. További információk: <https://github.com/coreybutler/nvm-windows>.

- A Node.js egy adott verziójának telepítése:

`nvm install {{node_version}}`

- A Node.js alapértelmezett verziójának beállítása (rendszergazdaként kell futtatni):

`nvm use {{node_version}}`

- Az összes elérhető Node.js verzió listázása és az alapértelmezett verzió kiemelése:

`nvm list`

- Az összes távoli Node.js verzió listázása:

`nvm ls-remote`

- Egy adott Node.js verzió eltávolítása:

`nvm uninstall {{node_version}}`
