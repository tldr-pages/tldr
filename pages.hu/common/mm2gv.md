# mm2gv

> Egy grafikon átalakítása Matrix Market `mm` formátumból `gv` formátumba. Konverterek: `gml2gv`, `gv2gml`, `gv2gxl`, `gxl2gv`, `graphml2gv` & `mm2gv`. További információ: <https://graphviz.org/pdf/mm2gv.1.pdf>.

- Egy grafikon átalakítása a `mm` formátumból a `gv` formátumba:

`mm2gv -o {{output.gv}} {{input.mm}}`

- Egy grafikon konvertálása a `stdin` és a `stdout` segítségével:

`cat {{input.mm}} | mm2gv > {{output.gv}}`

- Súgó megjelenítése:

`mm2gv -?`
