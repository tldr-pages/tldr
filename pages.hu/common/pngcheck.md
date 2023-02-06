# pngcheck

> A PNG, JNG és MNG fájlokkal kapcsolatos részletes információk nyomtatása és ellenőrzése. További információ: <http://www.libpng.org/pub/png/apps/pngcheck.html>.

- Összefoglaló nyomtatása egy képhez (szélesség, magasság és színmélység):

`pngcheck {{image.png}}`

- Információk nyomtatása egy képhez \[c\]olorizált kimenettel:

`pngcheck -c {{image.png}}`

- \[v\]erbose információ nyomtatása egy képhez:

`pngcheck -cvt {{image.png}}`

- Kép fogadása a `stdin` oldalról és részletes információk megjelenítése:

`cat {{path/to/image.png}} | pngcheck -cvt`

- \[s\]earch for PNGs within a specific file and display information about them:

`pngcheck -s {{image.png}}`

- PNG-k keresése egy másik fájlban, és azok \[x\]bemutatása:

`pngcheck -x {{image.png}}`
