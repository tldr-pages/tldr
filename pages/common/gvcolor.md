# gvcolor

> Colorize a ranked digraph with a range of colors.
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://graphviz.org/pdf/gvcolor.1.pdf>.

- Colorize one or more ranked digraph (that were already processed by `dot`):

`gvcolor {{path/to/layout1.gv}} {{path/to/layout2.gv ...}} > {{path/to/output.gv}}`

- Lay out a graph and colorize it, then convert to a PNG image:

`dot {{path/to/input.gv}} | gvcolor | dot -T {{png}} > {{path/to/output.png}}`

- Display help for `gvcolor`:

`gvcolor -?`
