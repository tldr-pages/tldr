# unflatten

> Az irányított gráfok beállítása az elrendezés oldalarányának javítása érdekében. Graphviz-szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://www.graphviz.org/pdf/unflatten.1.pdf.](https://www.graphviz.org/pdf/unflatten.1.pdf)

- Egy vagy több irányított gráf beállítása az elrendezés oldalarányának javítása érdekében:

`unflatten {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Használja a `unflatten` előfeldolgozóként a `dot` elrendezéshez a képarány javítása érdekében:

`unflatten {{path/to/input.gv}} | dot -T {{png}} {{path/to/output.png}}`

- A `unflatten` súgójának megjelenítése:

`unflatten -?`
