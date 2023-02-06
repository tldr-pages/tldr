# edgepaint

> A gráf elrendezés éleinek színezése a kereszteződő élek egyértelművé tétele érdekében. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://graphviz.org/pdf/edgepaint.1.pdf.](https://graphviz.org/pdf/edgepaint.1.pdf)

- Egy vagy több (már elrendezési információkkal rendelkező) gráf elrendezés éleinek színezése az egymást keresztező élek egyértelművé tétele érdekében:

`edgepaint {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Élek színezése egy színséma segítségével. ( [Lásd: https://graphviz.org/doc/info/colors.html#brewer)](https://graphviz.org/doc/info/colors.html#brewer):

`edgepaint -color-scheme={{accent7}} {{path/to/layout.gv}} > {{path/to/output.gv}}`

- Fektessen ki egy gráfot, és színezze ki az éleit, majd konvertálja PNG-képbe:

`dot {{path/to/input.gv}} | edgepaint | dot -T {{png}} > {{path/to/output.png}}`

- A `edgepaint` súgó megjelenítése:

`edgepaint -?`
