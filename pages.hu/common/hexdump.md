# hexdump

> ASCII, decimális, hexadecimális, oktális dump. További információ: <https://manned.org/hexdump>.

- Kinyomtatja egy fájl hexadecimális ábrázolását, a duplikált sorokat '\*'-mal helyettesíti:

`hexdump {{path/to/file}}`

- A bemeneti eltolás megjelenítése hexadecimális formában és annak ASCII ábrázolása két oszlopban:

`hexdump -C {{path/to/file}}`

- Megjeleníti egy fájl hexadecimális ábrázolását, de a bemenetnek csak n bájtját értelmezi:

`hexdump -C -n{{number_of_bytes}} {{path/to/file}}`

- A duplikált sorokat ne helyettesítse '\*'-mal:

`hexdump --no-squeezing {{path/to/file}}`
