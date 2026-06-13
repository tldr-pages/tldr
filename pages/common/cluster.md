# cluster

> Find clusters in a graph and augment the graph with this information.
> More information: <https://graphviz.org/pdf/cluster.1.pdf>.

- Generate clusters that optimize modularity and print the result to `stdout`:

`cluster {{input.gv}}`

- Specify a target number of [C]lusters (approximate) to generate (0 by default, meaning a number that approximately optimizes the modularity):

`cluster -C {{5}} {{input.gv}}`

- Use a different [c]lustering method (0: modularity clustering, 1: modularity quality):

`cluster -c {{0|1}} {{input.gv}}`

- Save the [o]utput to a file:

`cluster -o {{output.gv}} {{input.gv}}`

- Enable [v]erbose mode:

`cluster -v {{input.gv}}`
