# cluster

> Find clusters in a graph and augment the graph with this information.
> More information: <https://graphviz.org/pdf/cluster.1.pdf>.

- Generate clusters that optimize modularity and print the result to stdout:

`cluster {{input.gv}}`

- Specify a target number of clusters (approximate) to generate (0 by default):

`cluster -C {{5}} {{input.gv}}`

- Use a different clustering method (0: modularity clustering, 1: modularity quality):

`cluster -c {{1}} {{input.gv}}`

- Save the output to a file (default is stdout):

`cluster -o {{output.gv}} {{input.gv}}`

- Enable verbose mode:

`cluster -v {{input.gv}}`
