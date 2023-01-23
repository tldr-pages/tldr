# cwebp

> Képfájl tömörítése WebP-fájlba. További információ: <https://developers.google.com/speed/webp/docs/cwebp>.

- WebP fájl tömörítése alapértelmezett beállításokkal (q = 75) az \[o\]utput fájlba:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}}`

- WebP-fájl tömörítése a legjobb \[q\]ualitással és a legnagyobb fájlmérettel:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{100}}`

- A legrosszabb \[q\]ualitású és legkisebb fájlméretű WebP-fájl tömörítése:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{0}}`

- WebP fájl tömörítése és a kép méretének módosítása:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -resize {{width}} {{height}}`

- WebP-fájl tömörítése és az alfacsatorna-információ elhagyása:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -noalpha`
