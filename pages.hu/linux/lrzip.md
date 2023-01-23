# lrzip

> Nagyméretű fájlok tömörítésére szolgáló program. Lásd még: `lrunzip`, `lrztar`, `lrzuntar`. További információ: <https://manned.org/lrzip>.

- Fájl tömörítése LZMA-val - lassú tömörítés, gyors dekompresszió:

`lrzip {{filename}}`

- Fájl tömörítése BZIP2-vel - jó középút a tömörítés/gyorsaság tekintetében:

`lrzip -b {{filename}}`

- Tömörítés ZPAQ-val - extrém tömörítés, de nagyon lassú:

`lrzip -z {{filename}}`

- Tömörítés LZO-val - könnyű tömörítés, rendkívül gyors dekompresszió:

`lrzip -l {{filename}}`

- Tömörítés és jelszóvédelem/titkosítás:

`lrzip -e {{filename}}`

- A használandó processzorszálak számának felülbírálása:

`lrzip -p {{8}} {{filename}}`
