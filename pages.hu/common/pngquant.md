# pngquant

> PNG átalakító és veszteséges kép tömörítő. További információ: <https://pngquant.org/>.

- Egy adott PNG-t a lehető legnagyobb mértékben tömörít, és az eredményt egy új fájlba írja:

`pngquant {{path/to/file.png}}`

- Egy adott PNG tömörítése és az eredeti felülírása:

`pngquant --ext .png --force {{path/to/file.png}}`

- Próbáljon meg tömöríteni egy adott PNG-t egyéni minőséggel (kihagyja, ha a minimális érték alatt van):

`pngquant --quality {{0-100}} {{path/to/file.png}}`

- Egy adott PNG tömörítése a színek számának 64-re csökkentésével:

`pngquant {{64}} {{path/to/file.png}}`

- Egy adott PNG tömörítése és kihagyás, ha a fájl nagyobb, mint az eredeti:

`pngquant --skip-if-larger {{path/to/file.png}}`

- Egy adott PNG tömörítése és a metaadatok eltávolítása:

`pngquant --strip {{path/to/file.png}}`

- Egy adott PNG tömörítése és mentése a megadott elérési útvonalra:

`pngquant {{path/to/file.png}} --output {{path/to/file.png}}`

- Egy adott PNG tömörítése és a haladás megjelenítése:

`pngquant --verbose {{path/to/file.png}}`
