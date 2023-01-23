# coredumpctl

> A mentett core dumps és metaadatok lekérése és feldolgozása. További információ: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Az összes rögzített core dumps listázása:

`coredumpctl list`

- Egy programhoz rögzített core-dumpok listázása:

`coredumpctl list {{program}}`

- A `PID` címen a programhoz tartozó core dumps-ok információinak megjelenítése:

`coredumpctl info {{PID}}`

- A debugger meghívása egy program utolsó core dumpjának felhasználásával:

`coredumpctl debug {{program}}`

- Egy program utolsó core dumpjának kivonása egy fájlba:

`coredumpctl --output={{path/to/file}} dump {{program}}`
