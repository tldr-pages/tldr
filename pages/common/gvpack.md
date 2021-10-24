# gvpack

> Combine several graph layouts (that already have layout information).
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://graphviz.org/pdf/gvpack.1.pdf>.

- Combine several graph layouts (that already have layout information):

`gvpack {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Combine several graph layouts at the graph level, keeping graphs separate:

`gvpack -g {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Combine several graph layouts at the node level, ignoring clusters:

`gvpack -n {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Combine several graph layouts without packing:

`gvpack -u {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Display help for `gvpack`:

`gvpack -?`
