# gvgen

> Generate simple, structured abstract graphs.
> More information: <https://graphviz.org/pdf/gvgen.1.pdf>.

- Generate a cycle with 10 vertices and edges:

`gvgen -c {{10}}`

- Generate a 4×3 grid:

`gvgen -g {{4,3}}`

- Generate a binary tree of height 5:

`gvgen -t {{5}}`

- Generate a complete bipartite graph with 3 and 4 vertices:

`gvgen -b {{3,4}}`

- Create a random graph and write it to a file:

`gvgen -r {{10,5}} -o {{random.gv}}`

- Generate a directed graph with verbose output:

`gvgen -d -v -c {{6}}`

- Display help:

`gvgen -?`
