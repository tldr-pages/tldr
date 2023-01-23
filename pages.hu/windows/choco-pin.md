# choco pin

> A Chocolatey segítségével egy csomagot egy adott verzióhoz rögzíthet. A rögzített csomagok automatikusan kihagyásra kerülnek frissítéskor. További információ: <https://chocolatey.org/docs/commands-pin>.

- A kitűzött csomagok és verzióik listájának megjelenítése:

`choco pin list`

- Csatlakoztasson egy csomagot az aktuális verziójához:

`choco pin add --name {{package}}`

- Csomagok kitűzése egy adott verzióhoz:

`choco pin add --name {{package}} --version {{version}}`

- Egy adott csomag kitűzésének eltávolítása:

`choco pin remove --name {{package}}`
