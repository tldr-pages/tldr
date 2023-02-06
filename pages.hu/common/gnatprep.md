# gnatprep

> Előfeldolgozó az Ada forráskódfájlokhoz (a GNAT toolchain része). További információ: <https://gcc.gnu.org/onlinedocs/gnat_ugn/Preprocessing-with-gnatprep.html>.

- Szimbólumdefiníciók használata egy fájlból:

`gnatprep {{source_file}} {{target_file}} {{definitions_file}}`

- Szimbólumértékek megadása a parancssorban:

`gnatprep -D{{name}}={{value}} {{source_file}} {{target_file}}`
