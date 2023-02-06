# zsteg

> Steganográfia detektáló eszköz PNG és BMP fájlformátumokhoz. Felismeri az LSB steganográfiát, ZLIB tömörített adatokat, OpenStego, Camouflage és LSB az Eratosthenes készlettel. További információ: <https://github.com/zed-0xff/zsteg>.

- Beágyazott adatok felismerése PNG-ben:

`zsteg {{path/to/image.png}}`

- Beágyazott adatok észlelése egy BMP-képben, az összes ismert módszerrel:

`zsteg --all {{path/to/image.bmp}}`

- Beágyazott adatok felismerése egy PNG-képben, a pixelek függőleges iterációjával és az MSB-t használva először:

`zsteg --msb --order yx {{path/to/image.png}}`

- Beágyazott adatok felismerése BMP-képben, a figyelembe veendő bitek megadásával:

`zsteg --bits {{1,2,3|1-3}} {{path/to/image.bmp}}`

- Beágyazott adatok felderítése PNG-képben, csak a prím pixelek kivonása és a bitek invertálása:

`zsteg --prime --invert {{path/to/image.png}}`

- Beágyazott adatok felderítése BMP-képben, a keresendő karakterláncok minimális hosszának és a keresési módnak a megadása:

`zsteg --min-str-len {{10}} --strings {{first|all|longest|none}} {{path/to/image.bmp}}`
