# gxl2gv

> Egy grafikon átalakítása a `gxl` formátumból a `gv` formátumba. Konverterek: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. További információ: <https://graphviz.org/pdf/gxl2gv.1.pdf>.

- Egy grafikon átalakítása a `gxl` formátumból a `gv` formátumba:

`gxl2gv -o {{output.gv}} {{input.gxl}}`

- Egy grafikon átalakítása a `stdin` és a `stdout` segítségével:

`cat {{input.gxl}} | gxl2gv > {{output.gv}}`

- Súgó megjelenítése:

`gxl2gv -?`
