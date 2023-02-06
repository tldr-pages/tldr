# pngcheck

> Törvényszéki eszköz PNG alapú (`.png`, `.jng`, `.mng`) képfájlok integritásának ellenőrzésére. Képes beágyazott képeket és szöveget is kinyerni a fájlból. További információ: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Képfájlok integritásának ellenőrzése:

`pngcheck {{path/to/file.png}}`

- A fájl ellenőrzése \[v\]erbose és \[c\]olorizált kimenettel:

`pngcheck -vc {{path/to/file.png}}`

- A \[t\]ext chunks tartalmának megjelenítése és \[s\]earch for PNGs egy adott fájlon belül:

`pngcheck -ts {{path/to/file.png}}`

- Beágyazott PNG-k keresése és e\[x\]nyomozása egy adott fájlban:

`pngcheck -x {{path/to/file.png}}`
