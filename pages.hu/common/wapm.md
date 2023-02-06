# wapm

> A WebAssembly csomagkezelő. További információ: <https://wapm.io/help/reference>.

- Interaktívan hozzon létre egy új `wapm.toml` fájlt:

`wapm init`

- Töltse le a `wapm.toml` oldalon függőségként felsorolt összes csomagot:

`wapm install`

- Egy csomag egy adott verziójának letöltése és hozzáadása a wapm.toml függőségi listájához:

`wapm install {{package_name}}@{{version}}`

- Egy csomag letöltése és globális telepítése:

`wapm install --global {{package_name}}`

- Egy csomag eltávolítása és eltávolítása a `wapm.toml` függőségi listájáról:

`wapm uninstall {{package_name}}`

- A helyileg telepített függőségek fájának kinyomtatása:

`wapm list`

- A globálisan telepített csomagok legfelső szintű listája:

`wapm list --global`

- Egy csomagparancs végrehajtása a Wasmer futtatási idővel:

`wapm run {{command_name}} {{arguments}}`
