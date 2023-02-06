# neato

> A `linear undirected` hálózati gráf képének renderelése a `graphviz` fájlból. Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` és `patchwork`. További információ: <https://graphviz.org/doc/info/command.html>.

- Renderel egy `png` képet a bemeneti fájlnév és a kimeneti formátum (nagybetűs -O) alapján:

`neato -T {{png}} -O {{path/to/input.gv}}`

- A `svg` kép renderelése a megadott kimeneti fájlnévvel (kisbetűs -o):

`neato -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- A kimeneti képet a `ps`, `pdf`, `svg`, `fig`, `png`, `gif`, `jpg`, `json` vagy `dot` formátumban rendereli:

`neato -T {{format}} -O {{path/to/input.gv}}`

- A `gif` kép renderelése a `stdin` és a `stdout` segítségével:

`echo "{{graph {this -- that} }}" | neato -T {{gif}} > {{path/to/image.gif}}`

- Súgó megjelenítése:

`neato -?`
