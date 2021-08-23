# bcomps

> Discompose graphs into their biconnected components.
> Graphviz filters: `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> More information: <https://graphviz.org/pdf/bcomps.1.pdf>.

- Discompose graphs into their biconnected components:

`bcomps {{path/to/input1.gv}} {{path/to/input2.gv}} > {{path/to/output.gv}}`

- Print the number of blocks and cutvertice, producing no output graph:

`bcomps -v -s {{path/to/input1.gv}} {{path/to/input2.gv}}`

- Write each block and block-cutvertex tree to numbered filenames based on `output.gv`:

`bcomps -x -o {{path/to/output.gv}} {{path/to/input1.gv}} {{path/to/input2.gv}}`

- Display help:

`bcomps -?`
