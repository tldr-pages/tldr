# xxd

> Hexadecimális ábrázolás létrehozása (hexdump) bináris fájlból, vagy fordítva. További információ: <https://manned.org/xxd>.

- Hexdump generálása bináris fájlból és a kimenet megjelenítése:

`xxd {{input_file}}`

- Hexdump generálása bináris fájlból és mentése szöveges fájlként:

`xxd {{input_file}} {{output_file}}`

- Kompaktabb kimenet megjelenítése, az egymást követő nullák (ha vannak) csillaggal való helyettesítése:

`xxd -a {{input_file}}`

- A kimenet megjelenítése 10, egyenként egy oktett (byte) oszlopban:

`xxd -c {{10}} {{input_file}}`

- Csak 32 bájt hosszúságig jeleníti meg a kimenetet:

`xxd -l {{32}} {{input_file}}`

- A kimenetet egyszerű módban, az oszlopok közötti hézagok nélkül jeleníti meg:

`xxd -p {{input_file}}`

- Visszafordítja a hexdumpot binárisra, és bináris fájlként menti el:

`xxd -r -p {{input_file}} {{output_file}}`
