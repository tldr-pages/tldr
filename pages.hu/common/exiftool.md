# exiftool

> Fájlok metainformációinak olvasása és írása. További információ: <https://exiftool.org>.

- Egy adott fájl EXIF metaadatainak kinyomtatása:

`exiftool {{path/to/file}}`

- Az összes EXIF metaadat eltávolítása az adott fájlokból:

`exiftool -All= {{path/to/file1 path/to/file2 ...}}`

- GPS EXIF metaadatok eltávolítása adott képfájlokból:

`exiftool "-gps*=" {{path/to/image1 path/to/image2 ...}}`

- Az összes EXIF metaadat eltávolítása az adott képfájlokból, majd a szín és tájolás metaadatainak újbóli hozzáadása:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{image1 image2 ...}}`

- A könyvtárban lévő összes fénykép készítésének dátumát 1 órával előre mozgatja:

`exiftool "-AllDates+=0:0:0 1:0:0" {{path/to/directory}}`

- Az aktuális könyvtárban lévő összes JPEG-fotó készítésének dátumát 1 nappal és 2 órával hátrébb helyezi:

`exiftool "-AllDates-=0:0:1 2:0:0" -ext jpg`

- Csak a `DateTimeOriginal` mező módosítása 1,5 óra levonásával, biztonsági mentések megtartása nélkül:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- A `DateTimeOriginal` mező alapján rekurzívan átnevezi az összes JPEG-fényképet egy könyvtárban:

`exiftool '-filename<DateTimeOriginal' -d %Y-%m-%d_%H-%M-%S%%lc.%%e {{path/to/directory}} -r -ext jpg`
