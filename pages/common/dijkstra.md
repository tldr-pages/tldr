# dijkstra

> Compute shortest-path distances from a single source node in a graph.
> Reads graphs, computes distances, and sets node and graph attributes such as `dist`, `prev`, and `maxdist`.
> More information: <https://graphviz.org/pdf/dijkstra.1.pdf>.

- Compute distances from a given source node in a graph file:

`dijkstra {{source_node file}}`

- Treat the graph as directed when computing distances:

`dijkstra -d {{source_node file}}`

- Set each node reachable from source_node to it's distance from the source_node:

`dijkstra -p {{source_node file}}`

- Assign large distance values to unreachable nodes:

`dijkstra -a {{source_node file}}`
