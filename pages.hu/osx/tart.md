# tart

> MacOS és Linux virtuális gépek (VM-ek) készítése, futtatása és kezelése Apple Silicon-on. További információk: <https://github.com/cirruslabs/tart>.

- Távoli VM-kép lehívása:

`tart pull {{acme.io/org/name:tag}}`

- VM klónozása helyi vagy távoli képforrásból:

`tart clone {{source-vm}} {{vm-name}}`

- Új Mac VM létrehozása egy adott ipsw fájlból:

`tart create --from-ipsw={{latest|path/to/file.ipsw}} {{vm-name}}`

- Egy meglévő VM futtatása:

`tart run {{vm-name}}`

- Meglévő VM futtatása egy adott beágyazott könyvtárral:

`tart run --dir={{path/to/directory}}:{{/path/to/local_directory}} {{vm-name}}`

- VM-ek listázása:

`tart list`

- Egy futó VM IP-címének lekérdezése:

`tart ip {{vm-name}}`

- VM kijelzőfelbontásának módosítása:

`tart set {{vm-name}} --display {{width}}x{{height}}`
