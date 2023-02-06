# nop

> Érvényesség ellenőrzése és grafikonok kanonikus formátumban történő szépnyomtatása. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://www.graphviz.org/pdf/nop.1.pdf.](https://www.graphviz.org/pdf/nop.1.pdf)

- Egy vagy több gráf kanonikus formátumban történő szépnyomtatása:

`nop {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Egy vagy több gráf érvényességének ellenőrzése, kimeneti gráf előállítása nélkül:

`nop -p {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- A `nop` súgójának megjelenítése:

`nop -?`
