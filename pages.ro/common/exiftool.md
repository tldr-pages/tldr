# exiftool

> Citiți și scrieți informații meta în fișiere.
> Mai multe informaţii: <https://exiftool.org>

- Eliminați toate metadatele EXIF din fișierele date:

`exiftool -All= {{file1 file2 ...}}`

- Mutați data la care toate fotografiile dintr-un director au fost luate cu o oră înainte:

`exiftool "-AllDates+=0:0:0 1:0:0" {{path/to/directory}}`

- Mutați data la care toate fotografiile JPEG din directorul curent au fost realizate cu o zi și 2 ore înapoi:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Modificați doar câmpul `datetimeOriginal` scăzând 1,5 ore, fără a păstra copii de rezervă:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Redenumiți recursiv toate fotografiile JPEG într-un director bazat pe câmpul `datetimeOriginal`:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{path/to/directory}} -r -ext jpg`
