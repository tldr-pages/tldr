# gvmap

> Find clusters and creates a geographical map highlighting clusters.
> More information: <https://graphviz.org/pdf/gvmap.1.pdf>.

- Generate a clustered map layout from a DOT format graph:

`gvmap {{graph.gv}} -o {{output.xdot}}`

- Generate a map using existing cluster subgraphs from the input:

`gvmap -D {{graph.gv}}`

- Include graph edges in the [o]utput map:

`gvmap -e {{graph.gv}} -o {{output.xdot}}`

- Specify a [c]olor scheme (1: pastel, 2: blue-yellow, 3: white-red, etc.):

`gvmap -c {{1|2|3|...}} {{graph.gv}} -o {{output.xdot}}`

- Set the maximum number of [C]lusters (by default 0, meaning there is no limit):

`gvmap -C {{10}} {{graph.gv}} -o {{output.xdot}}`

- Only draw cluster 2 (by default, all clusters are drawn):

`gvmap -highlight={{2}} {{graph.gv}} -o {{output.xdot}}`
