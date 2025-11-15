# abbr

> Gestiona abreviatures per la shell fish.
> Les paraules definides per l'usuari es reemplacen per expresions llarges en introduïr-les.
> Més informació: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Afegeix una nova abreviatura:

`abbr --add {{nom_abreviatura}} {{comandament}} {{arguments}}`

- Canvia el nom d'una abreviatura existent:

`abbr --rename {{antic_nom}} {{nou_nom}}`

- Esborra una abreviatura existent:

`abbr --erase {{nom_abreviatura}}`

- Importa les abreviatures definides en un altre host per SSH:

`ssh {{nom_host}} abbr --show | source`
