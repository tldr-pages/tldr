# gv2gxl

> Egy grafikon átalakítása a `gv` formátumból a `gxl` formátumba. Konverterek: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. További információ: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Egy grafikon átalakítása a `gv` formátumból a `gxl` formátumba:

`gv2gxl -o {{output.gxl}} {{input.gv}}`

- Egy grafikon átalakítása a `stdin` és a `stdout` segítségével:

`cat {{input.gv}} | gv2gxl > {{output.gxl}}`

- Súgó megjelenítése:

`gv2gxl -?`
