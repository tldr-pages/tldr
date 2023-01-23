# npm

> JavaScript és Node.js csomagkezelő. Node.js projektek és modulfüggőségeik kezelése. További információk: <https://www.npmjs.com>.

- Interaktívan hozzon létre egy `package.json` fájlt:

`npm init`

- Töltse le a package.json fájlban függőségként felsorolt összes csomagot:

`npm install`

- Egy csomag egy adott verziójának letöltése és hozzáadása a `package.json` függőségi listához:

`npm install {{module_name}}@{{version}}`

- Egy csomag letöltése és hozzáadása a dev függőségek listájához a `package.json`:

`npm install {{module_name}} --save-dev`

- Egy csomag letöltése és globális telepítése:

`npm install --global {{module_name}}`

- Egy csomag eltávolítása és eltávolítása a `package.json` függőségi listájáról:

`npm uninstall {{module_name}}`

- A helyileg telepített függőségek fájának kinyomtatása:

`npm list`

- Felső szintű globálisan telepített modulok listázása:

`npm list --global --depth={{0}}`
