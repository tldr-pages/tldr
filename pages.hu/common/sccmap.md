# sccmap

> Irányított gráfok erősen összefüggő összetevőinek kivonása. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: <https://www.graphviz.org/pdf/sccmap.1.pdf>.

- Egy vagy több irányított gráf erősen összefüggő összetevőinek kivonása:

`sccmap -S {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Statisztikák nyomtatása egy gráfról, kimeneti gráf előállítása nélkül:

`sccmap -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- A `sccmap` súgó megjelenítése:

`sccmap -?`
