# dwebp

> `dwebp` a WebP fájlokat PNG, PAM, PPM vagy PGM képekre dekomprimálja. Az animált WebP fájlok nem támogatottak. További információ: <https://developers.google.com/speed/webp/docs/dwebp/>.

- A `webp` fájl átalakítása `png` fájlba:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}}`

- A `webp` fájl átalakítása egy adott fájltípussá:

`dwebp {{path/to/input.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{path/to/output}}`

- Konvertáljon egy `webp` fájlt, lehetőség szerint többszálú feldolgozással:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -mt`

- Konvertáljon egy `webp` fájlt, de egyidejűleg vágja és méretezze is:

`dwebp {{input.webp}} -o {{output.png}} -crop {{x_pos}} {{y_pos}} {{width}} {{height}} -scale {{width}} {{height}}`

- Egy `webp` fájl átalakítása és a kimenet megfordítása:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -flip`

- Konvertáljon egy `webp` fájlt, és ne használjon hurokon belüli szűrést a dekódolási folyamat felgyorsítása érdekében:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -nofilter`
