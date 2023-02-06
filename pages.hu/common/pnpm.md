# pnpm

> Gyors, lemezterület-hatékony csomagkezelő a Node.js számára. Node.js projektek és modulfüggőségeik kezelése. További információ: <https://pnpm.io>.

- Hozzon létre egy `package.json` fájlt:

`pnpm init`

- Töltse le a `package.json` oldalon függőségként felsorolt összes csomagot:

`pnpm install`

- Egy csomag egy adott verziójának letöltése és hozzáadása a `package.json` függőségi listájához:

`pnpm add {{module_name}}@{{version}}`

- Töltsön le egy csomagot, és adja hozzá a \[D\]ev függőségek listájához a `package.json` oldalon:

`pnpm add -D {{module_name}}`

- Egy csomag letöltése és telepítése \[g\]lobálisan:

`pnpm add -g {{module_name}}`

- Egy csomag eltávolítása és eltávolítása a `package.json` függőségi listájáról:

`pnpm remove {{module_name}}`

- A helyileg telepített modulok fájának kinyomtatása:

`pnpm list`

- A legfelső szintű \[g\]lobally telepített modulok listája:

`pnpm list -g --depth={{0}}`
