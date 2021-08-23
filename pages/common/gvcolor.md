# gvcolor

> Flow colors through a ranked digraph (that was already processed by `dot`).
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://graphviz.org/pdf/gvcolor.1.pdf>.

- Flow colors through a ranked digraph (that was already processed by `dot`):

`gvcolor {{path/to/layout1.gv}} {{path/to/layout2.gv}} > {{path/to/output.gv}}`

- Perform layout, colorization, and output to a picture with one command:

`dot {{path/to/input.gv}} | gvcolor | dot -T {{png}} > {{path/to/output.png}}`

- Display help:

`gvcolor -?`
