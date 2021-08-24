# ccomps

> Decompose graphs into their connected components.
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://graphviz.org/pdf/ccomps.1.pdf>.

- Decompose one or more graphs into their connected components:

`ccomps {{path/to/input1.gv}} {{path/to/input2.gv ...}} > {{path/to/output.gv}}`

- Print the number of nodes, edges, and connected components in one or more graphs:

`ccomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- Write each connected component to numbered filenames based on `output.gv`:

`ccomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv ...}}`

- Display help for `ccomps`:

`ccomps -?`
