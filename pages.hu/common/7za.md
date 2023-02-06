# 7za

> Nagy tömörítési aránnyal rendelkező fájlarchiváló. Hasonló a `7z` -hoz, de kevesebb fájltípust támogat, viszont keresztplatformos. További információ: <https://www.7-zip.org>.

- \[a\]rchive a file or directory:

`7za a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- Egy meglévő archívum titkosítása (beleértve a fájlneveket is):

`7za a {{path/to/encrypted.7z}} -p{{password}} -mhe={{on}} {{path/to/archive.7z}}`

- E\[x\]traktálni egy archívumot az eredeti könyvtárszerkezet megőrzésével:

`7za x {{path/to/archive.7z}}`

- E\[x\]tract an archive to a specific directory:

`7za x {{path/to/archive.7z}} -o{{path/to/output}}`

- E\[x\]tract an archive to `stdout`:

`7za x {{path/to/archive.7z}} -so`

- \[a\]rchiválás egy adott archívumtípussal:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- \[l\]ist az archívum tartalma:

`7za l {{path/to/archive.7z}}`

- A rendelkezésre álló archívumtípusok listája:

`7za i`
