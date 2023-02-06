# steam

> A Valve videojáték-platformja. További információ: <https://developer.valvesoftware.com/wiki/Command_Line_Options>.

- A Steam elindítása, hibakeresési üzenetek nyomtatása a `stdout` címre:

`steam`

- Indítsa el a Steamet, és kapcsolja be az alkalmazáson belüli hibakereső konzol lapot:

`steam -console`

- Engedélyezze és nyissa meg a Steam konzol lapját egy futó Steam példányban:

`steam steam://open/console`

- Jelentkezzen be a Steambe a megadott hitelesítő adatokkal:

`steam -login {{username}} {{password}}`

- Indítsa el a Steamet Big Picture módban:

`steam -tenfoot`

- Kilépés a Steamből:

`steam -shutdown`
