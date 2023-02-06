# mingle

> Egy gráf elrendezés éleinek összevonása. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://www.graphviz.org/pdf/mingle.1.pdf.](https://www.graphviz.org/pdf/mingle.1.pdf)

- Egy vagy több (már elrendezési információkkal rendelkező) gráfelrendezés éleinek összevonása:

`mingle {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Egyetlen paranccsal végezheti el az elrendezést, a kötegelést és a képre történő kimenetet:

`dot {{path/to/input.gv}} | mingle | dot -T {{png}} > {{path/to/output.png}}`

- A `mingle` súgójának megjelenítése:

`mingle -?`
