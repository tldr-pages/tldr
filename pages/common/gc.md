
# gc

> Count nodes, edges, connected components, or clusters in Graphviz `.dot` files.
> By default, prints number of nodes and edges.
> More information: <https://graphviz.org/pdf/gc.1.pdf>.

- Count nodes and edges in a file:

`gc {{path/to/file.dot}}`

- Count only nodes:

`gc -n {{path/to/file.dot}}`

- Count only edges:

`gc -e {{path/to/file.dot}}`

- Count connected components:

`gc -c {{path/to/file.dot}}`

- Display help:

`gc -?`
