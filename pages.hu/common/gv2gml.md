# gv2gml

> Egy grafikon átalakítása a `gv` formátumból a `gml` formátumba. Konverterek: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. További információ: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- Egy grafikon átalakítása a `gv` formátumból a `gml` formátumba:

`gv2gml -o {{output.gml}} {{input.gv}}`

- Egy grafikon átalakítása a `stdin` és a `stdout` segítségével:

`cat {{input.gv}} | gv2gml > {{output.gml}}`

- Súgó megjelenítése:

`gv2gml -?`
