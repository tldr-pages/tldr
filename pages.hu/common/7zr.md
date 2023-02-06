# 7zr

> Nagy tömörítési aránnyal rendelkező fájlarchiváló. Hasonló a `7z` -hoz, kivéve, hogy csak a `.7z` fájlokat támogatja. További információ: <https://www.7-zip.org>.

- \[a\]rchive a file vagy directory:

`7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- Egy meglévő archívum titkosítása (beleértve a fájlneveket is):

`7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}`

- E\[x\]tract egy archívumot az eredeti könyvtárstruktúra megőrzésével:

`7zr x {{path/to/archive.7z}}`

- E\[x\]traktálni egy archívumot egy adott könyvtárba:

`7zr x {{path/to/archive.7z}} -o{{path/to/output}}`

- E\[x\]tract an archive to `stdout`:

`7zr x {{path/to/archive.7z}} -so`

- \[l\]ist egy archívum tartalma:

`7zr l {{path/to/archive.7z}}`

- A rendelkezésre álló archívumtípusok listája:

`7zr i`
