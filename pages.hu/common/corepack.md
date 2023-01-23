# corepack

> Nulla futásidő-függőségű csomag, amely hídként működik a Node projektek és csomagkezelőik között. További információ: <https://github.com/nodejs/corepack>.

- Adja hozzá a Corepack shimeket a Node.js telepítési könyvtárához, hogy globális parancsként elérhetővé váljanak:

`corepack enable`

- Adja hozzá a Corepack shimeket egy adott könyvtárhoz:

`corepack enable --install-directory {{path/to/directory}}`

- A Corepack shimek eltávolítása a Node.js telepítési könyvtárából:

`corepack disable`

- Egy adott csomagkezelő előkészítése:

`corepack prepare {{package_manager}}@{{version}} --activate`

- Az aktuális elérési útvonalban lévő projekthez konfigurált csomagkezelő előkészítése:

`corepack prepare`

- Egy csomagkezelő használata anélkül, hogy globális parancsként telepítené:

`corepack {{npm|pnpm|yarn}} {{package_manager_arguments}}`

- Csomagkezelő telepítése a megadott archívumból:

`corepack hydrate {{path/to/corepack.tgz}}`

- Súgó megjelenítése egy alparancshoz:

`corepack {{subcommand}} --help`
