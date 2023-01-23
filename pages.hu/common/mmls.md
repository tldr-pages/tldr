# mmls

> A kötetrendszer partícióelrendezésének megjelenítése. További információ: <https://wiki.sleuthkit.org/index.php?title=Mmls>.

- A lemezképfájlban tárolt partíciós tábla megjelenítése:

`mmls {{path/to/image_file}}`

- A partíciós tábla megjelenítése a partíció méretére vonatkozó kiegészítő oszloppal:

`mmls -B -i {{path/to/image_file}}`

- A felosztott EWF-képben lévő partíciós tábla megjelenítése:

`mmls -i ewf {{image.e01}} {{image.e02}}`

- Beágyazott partíciós táblák megjelenítése:

`mmls -t {{nested_table_type}} -o {{offset}} {{path/to/image_file}}`
