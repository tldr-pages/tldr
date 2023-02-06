# bcomps

> Gráfok biconnected összetevőikre bontása. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: <https://graphviz.org/pdf/bcomps.1.pdf>.

- Egy vagy több gráf biconnected komponensekre bontása:

`bcomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Egy vagy több gráfban lévő blokkok és vágott csúcsok számának kiírása:

`bcomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- Írja ki az egyes blokkokat és blokk-vágóvertex fákat több számozott fájlnévre a `output.gv` alapján:

`bcomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- A `bcomps` súgójának megjelenítése:

`bcomps -?`
