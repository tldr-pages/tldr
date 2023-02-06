# homectl

> A systemd-homed szolgáltatás segítségével létrehozhat, eltávolíthat, módosíthat vagy ellenőrizhet főkönyvtárakat. További információ: <https://manned.org/homectl>.

- Felhasználói fiókok és a hozzájuk tartozó otthoni könyvtárak listázása:

`homectl list`

- Felhasználói fiókok és a hozzájuk tartozó home könyvtárak létrehozása:

`sudo homectl create {{username}}`

- Egy adott felhasználó és a hozzá tartozó home könyvtár eltávolítása:

`sudo homectl remove {{username}}`

- Egy adott felhasználó jelszavának módosítása:

`sudo homectl passwd {{username}}`

- Shell vagy parancs futtatása egy adott home könyvtárhoz való hozzáféréssel:

`sudo homectl with {{username}} -- {{command}} {{command_arguments}}`

- Egy adott home könyvtár zárolása vagy feloldása:

`sudo homectl {{lock|unlock}} {{username}}`

- Egy adott home könyvtárhoz rendelt lemezterület 100 GiB-ra történő módosítása:

`sudo homectl resize {{username}} {{100G}}`

- Súgó megjelenítése:

`homectl --help`
