# dijkstra

> Compute shortest-path distances from a single source node in a graph.
> More information: <https://graphviz.org/pdf/dijkstra.1.pdf>.

- Compute distances from a given source node in a graph file:

`dijkstra {{source_node_file}}`

- Treat the graph as [d]irected when computing distances:

`dijkstra -d {{source_node_file}}`

- Record the [p]revious closest node for each node on the shortest path:

`dijkstra -p {{source_node_file}}`

- [a]ssign large distance values to unreachable nodes:

`dijkstra -a {{source_node_file}}`
