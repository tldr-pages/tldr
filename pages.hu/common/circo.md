# circo

> A `circular` hálózati gráf képének renderelése a `graphviz` fájlból. Layouts: `dot`, `neato`, `twopi`, `circo`, `fdp`, `sfdp`, `osage` és `patchwork`. További információ: <https://graphviz.org/doc/info/command.html>.

- Renderel egy `png` képet a bemeneti fájlnév és a kimeneti formátum (nagybetűs -O) alapján:

`circo -T {{png}} -O {{path/to/input.gv}}`

- A `svg` kép renderelése a megadott kimeneti fájlnévvel (kisbetűs -o):

`circo -T {{svg}} -o {{path/to/image.svg}} {{path/to/input.gv}}`

- A kimeneti képet a `ps`, `pdf`, `svg`, `fig`, `png`, `gif`, `jpg`, `json` vagy `dot` formátumban rendereli:

`circo -T {{format}} -O {{path/to/input.gv}}`

- A `gif` kép renderelése a `stdin` és a `stdout` segítségével:

`echo "{{digraph {this -> that} }}" | circo -T {{gif}} > {{path/to/image.gif}}`

- Súgó megjelenítése:

`circo -?`
