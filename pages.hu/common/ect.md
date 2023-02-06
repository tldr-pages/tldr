# ect

> Hatékony tömörítő eszköz. C++ nyelven írt fájloptimalizáló. Támogatja a `.png`, `.jpg`, `.gzip` és `.zip` fájlokat. További információ: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Egy fájl tömörítése:

`ect {{path/to/file.png}}`

- Egy fájl tömörítése megadott tömörítési szinttel és többszálú tömörítéssel (1=Gyorsabb (Legrosszabb), 9=Lassabb (Legjobb), alapértelmezett a 3):

`ect -{{9}} --mt-deflate {{path/to/file.zip}}`

- Egy könyvtár összes fájljának rekurzív tömörítése:

`ect -recurse {{path/to/directory}}`

- Egy fájl tömörítése az eredeti módosítási idő megtartásával:

`ect -keep {{path/to/file.png}}`

- Egy fájl tömörítése a metaadatok eltávolításával:

`ect -strip {{path/to/file.png}}`
