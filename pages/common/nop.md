# nop

> Check validity and pretty-print graphs in canonical format.
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://www.graphviz.org/pdf/nop.1.pdf>.

- Pretty-print one or more graphs in canonical format:

`nop {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Check one or more graphs for validity, producing no output graph:

`nop -p {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- Display help:

`nop -?`
