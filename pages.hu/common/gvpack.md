# gvpack

> Több (már elrendezési információkkal rendelkező) grafikon elrendezés kombinálása. Graphviz szűrők: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`. További információ: [https://graphviz.org/pdf/gvpack.1.pdf.](https://graphviz.org/pdf/gvpack.1.pdf)

- Több (már elrendezési információval rendelkező) grafikon elrendezés kombinálása:

`gvpack {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Több gráf elrendezés kombinálása gráfszinten, a gráfok külön tartásával:

`gvpack -g {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Több gráf elrendezés kombinálása a csomópontok szintjén, a klaszterek figyelmen kívül hagyásával:

`gvpack -n {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Több gráf elrendezés kombinálása csomagolás nélkül:

`gvpack -u {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- A `gvpack` súgó megjelenítése:

`gvpack -?`
