# fossil commit

> Fájlok commitolása egy Fossil repositoryba. További információ: <https://fossil-scm.org/home/help/commit>.

- Új verzió létrehozása, amely tartalmazza az aktuális ellenőrzésben lévő összes változtatást; a felhasználótól kérni fog egy megjegyzést:

`fossil commit`

- Új verzió létrehozása, amely tartalmazza az aktuális checkout összes módosítását, a megadott megjegyzés felhasználásával:

`fossil commit --comment "{{comment}}"`

- Új verzió létrehozása, amely tartalmazza az aktuális checkout összes módosítását egy adott fájlból beolvasott megjegyzéssel:

`fossil commit --message-file {{path/to/commit_message_file}}`

- Új verzió létrehozása, amely a megadott fájlok változásait tartalmazza; a felhasználónak meg kell adnia a megjegyzést:

`fossil commit {{path/to/file1}} {{path/to/file2}}`
