# zsteg

> Instrument de detectare Steganografie pentru formatele de fișiere PNG și BMP.
> Detectează steganografia LSB, datele comprimate ZLIB-, OpensTego, Camouflage și LSB cu setul Eratostene.
> Mai multe informaţii: <https://github.com/zed-0xff/zsteg>

- Detectați datele încorporate într-o imagine PNG:

`zsteg {{path/to/image.png}}`

- Detectați datele încorporate într-o imagine BMP, utilizând toate metodele cunoscute:

`zsteg --all {{path/to/image.bmp}}`

- Detectați datele încorporate într-o imagine PNG, iterând pixelii vertical și utilizând mai întâi MSB:

`zsteg --msb --order yx {{path/to/image.png}}`

- Detectați datele încorporate într-o imagine BMP, specificând biții de luat în considerare:

`zsteg --bits {{1,2,3|1-3}} {{path/to/image.bmp}}`

- Detectează datele încorporate într-o imagine PNG, extragând numai pixelii prime şi inversând biţii:

`zsteg --prime --invert {{path/to/image.png}}`

- Detectați datele încorporate într-o imagine BMP, specificând lungimea minimă a șirurilor de găsit și modul de găsire:

`zsteg --min-str-len {{10}} --strings {{first|all|longest|none}} {{path/to/image.bmp}}`
