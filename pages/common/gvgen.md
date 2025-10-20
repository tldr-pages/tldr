# gvgen

> Generate simple, structured abstract graphs.
> More information: <https://graphviz.org/pdf/gvgen.1.pdf>.

- Generate a [c]ycle with 10 vertices and edges and write it to `stdout`:

`gvgen -c {{10}}`

- Generate a 4×3 [g]rid:

`gvgen -g {{4,3}}`

- Generate a binary [t]ree of height 5:

`gvgen -t {{5}}`

- Generate a complete [b]ipartite graph with 3 and 4 vertices:

`gvgen -b {{3,4}}`

- Create a [r]andom graph and [o]utput it to a file:

`gvgen -r {{10,5}} -o {{random.gv}}`

- Generate a [d]irected graph with [v]erbose output:

`gvgen -d -v -c {{6}}`

- Display help:

`gvgen -?`
