# bcomps

> Decompose graphs into their biconnected components.
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://graphviz.org/pdf/bcomps.1.pdf>.

- Decompose one or more graphs into their biconnected components:

`bcomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Print the number of blocks and cutvertices in one or more graphs:

`bcomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- Write each block and block-cutvertex tree to multiple numbered filenames based on `output.gv`:

`bcomps -x -o {{path/to/output.gv}} {{path/to/input1.gv path/to/input2.gv ...}}`

- Display help:

`bcomps -?`
