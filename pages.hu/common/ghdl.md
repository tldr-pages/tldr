# ghdl

> Nyílt forráskódú szimulátor a VHDL nyelvhez. További információ: <http://ghdl.free.fr>.

- VHDL forrásfájl elemzése és objektumfájl előállítása:

`ghdl -a {{filename.vhdl}}`

- Tervezet kidolgozása (ahol `{{design}}` egy konfigurációs egység, entitásegység vagy architektúraegység neve):

`ghdl -e {{design}}`

- A kidolgozott terv futtatása:

`ghdl -r {{design}}`

- Egy kidolgozott terv futtatása és a kimenet doppolása egy hullámforma-fájlba:

`ghdl -r {{design}} --wave={{output.ghw}}`

- Egy VHDL-forrásfájl szintaxisának ellenőrzése:

`ghdl -s {{filename.vhdl}}`

- A súgóoldal megjelenítése:

`ghdl --help`
