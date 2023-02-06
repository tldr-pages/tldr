# ccomps

> Gráfok szétbontása összefüggő összetevőikre. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: <https://graphviz.org/pdf/ccomps.1.pdf>.

- Egy vagy több gráf szétbontása összefüggő összetevőikre:

`ccomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Nyomtassa ki egy vagy több gráf csomópontjainak, éleinek és összefüggő komponenseinek számát:

`ccomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- Írja ki az egyes összefüggő komponenseket számozott fájlnevekbe a `output.gv` alapján:

`ccomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- A `ccomps` súgójának megjelenítése:

`ccomps -?`
