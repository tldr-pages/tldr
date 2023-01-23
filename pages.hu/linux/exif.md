# exif

> EXIF-információk megjelenítése és módosítása JPEG-fájlokban. További információ: <https://github.com/libexif/exif/>.

- Az összes felismert EXIF-információ megjelenítése egy képen:

`exif {{path/to/image.jpg}}`

- Megjelenít egy táblázatot, amely felsorolja az ismert EXIF-címkéket és azt, hogy mindegyik létezik-e a képen:

`exif --list-tags --no-fixup {{image.jpg}}`

- A kép miniatűrjének kivonása a fájlba `thumbnail.jpg`:

`exif --extract-thumbnail --output={{thumbnail.jpg}} {{image.jpg}}`

- A "Modell" címke nyers tartalmának megjelenítése az adott képen:

`exif --ifd={{0}} --tag={{Model}} --machine-readable {{image.jpg}}`

- Az "Artist" címke értékének módosítása John Smith-re és mentése a `new.jpg` címre:

`exif --output={{new.jpg}} --ifd={{0}} --tag="{{Artist}}" --set-value="{{John Smith}}" --no-fixup {{image.jpg}}`
