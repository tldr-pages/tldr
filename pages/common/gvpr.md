# gvpr

> A graph pattern scanning and processing language for Graphviz.
> It provides a way to query and transform graph structures using a pattern matching language.
> More information: <https://graphviz.org/pdf/gvpr.1.pdf>.

- Process a graph and write the result to an output file:

`gvpr {{path/to/input.gv}} > {{path/to/output.gv}}`

- Apply a transformation to relabel all nodes:

`gvpr -c 'N { $.label = "node_" + $.name; }' {{path/to/input.gv}} > {{path/to/output.gv}}`

- Delete all edges:

`gvpr -c 'E { delete($G, $); }' {{path/to/input.gv}} > {{path/to/output.gv}}`

- Select and print all nodes with a specific label:

`gvpr -c 'N { if ($.label == "{{target_label}}") print($.name); }' {{path/to/input.gv}}`

- Convert a graph to undirected:

`gvpr -c 'BEG_G { $G.directed = 0; }' {{path/to/input.gv}} > {{path/to/output.gv}}`

- Filter nodes by degree:

`gvpr -c 'N { if ($.outdegree > {{n}}) write($G); }' {{path/to/input.gv}} > {{path/to/output.gv}}`

- Display help information:

`gvpr -?`
