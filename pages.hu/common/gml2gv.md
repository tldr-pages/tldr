# gml2gv

> Egy grafikon átalakítása a `gml` formátumból a `gv` formátumba. Konverterek: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. További információ: <https://graphviz.org/pdf/gml2gv.1.pdf>.

- Egy grafikon átalakítása a `gml` formátumból a `gv` formátumba:

`gml2gv -o {{output.gv}} {{input.gml}}`

- Egy grafikon átalakítása a `stdin` és a `stdout` segítségével:

`cat {{input.gml}} | gml2gv > {{output.gv}}`

- Súgó megjelenítése:

`gml2gv -?`
