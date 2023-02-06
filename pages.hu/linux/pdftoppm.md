# pdftoppm

> PDF dokumentum oldalainak átalakítása hordozható Pixmap (képformátum) formátumba. További információ: <https://manned.org/pdftoppm>.

- Adja meg a konvertálandó oldalak tartományát (N-első oldal, M-utolsó oldal):

`pdftoppm -f {{N}} -l {{M}} {{path/to/file.pdf}} {{image_name_prefix}}`

- Csak a PDF dokumentum első oldalát konvertálja:

`pdftoppm -singlefile {{path/to/file.pdf}} {{image_name_prefix}}`

- Monokróm PBM fájl generálása (színes PPM fájl helyett):

`pdftoppm -mono {{path/to/file.pdf}} {{image_name_prefix}}`

- Szürkeárnyalatos PGM-fájl létrehozása (színes PPM-fájl helyett):

`pdftoppm -gray {{path/to/file.pdf}} {{image_name_prefix}}`

- PNG-fájl generálása PPM-fájl helyett:

`pdftoppm -png {{path/to/file.pdf}} {{image_name_prefix}}`
