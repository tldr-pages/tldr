# cvs

> Concurrent Versions System, egy revíziós ellenőrzési rendszer. További információ: <https://cvs.nongnu.org>.

- Új tároló létrehozása (a `CVSROOT` környezeti változó külső beállítását igényli):

`cvs -d {{path/to/repository}} init`

- Adjon hozzá egy projektet a tárolóhoz:

`cvs import -m "{{message}}" {{project_name}} {{version}} {{vendor}}`

- Egy projekt kijelentése:

`cvs checkout {{project_name}}`

- A fájlokban végrehajtott változtatások megjelenítése:

`cvs diff {{path/to/file}}`

- Fájl hozzáadása:

`cvs add {{path/to/file}}`

- Commit a file:

`cvs commit -m "{{message}}" {{path/to/file}}`

- A munkakönyvtár frissítése a távoli tárolóból:

`cvs update`
