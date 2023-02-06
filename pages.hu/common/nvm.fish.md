# nvm

> Telepítés, eltávolítás, vagy váltás a Node.js verziók között a `fish` héj alatt. Támogatja az olyan verziószámokat, mint "12.8" vagy "v16.13.1", és az olyan címkéket, mint "stable", "system", stb. További információ [: https://github.com/jorgebucaran/nvm.fish](https://github.com/jorgebucaran/nvm.fish).

- A Node.js egy adott verziójának telepítése:

`nvm install {{node_version}}`

- A Node.js egy adott verziójának használata az aktuális héjban:

`nvm use {{node_version}}`

- A Node.js alapértelmezett verziójának beállítása:

`set nvm_default_version {{node_version}}`

- Az összes elérhető Node.js verzió listázása és az alapértelmezett verzió kiemelése:

`nvm list`

- Egy adott Node.js verzió eltávolítása:

`nvm uninstall {{node_version}}`
