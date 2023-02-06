# gvcolor

> Rangsorolt digráf színezése különböző színekkel. Graphviz szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://graphviz.org/pdf/gvcolor.1.pdf.](https://graphviz.org/pdf/gvcolor.1.pdf)

- Egy vagy több rangsorolt digráf színezése (amelyeket a `dot` már feldolgozott):

`gvcolor {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Fektessen le egy gráfot és színezze ki, majd konvertálja PNG-képpé:

`dot {{path/to/input.gv}} | gvcolor | dot -T {{png}} > {{path/to/output.png}}`

- A `gvcolor` súgójának megjelenítése:

`gvcolor -?`
