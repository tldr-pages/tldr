# terraform graph

> Generate a visual representation of Terraform's resource dependency graph in Graphviz DOT format.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/graph>.

- Print the dependency graph for the current configuration in DOT format:

`terraform graph`

- Generate a graph for a specific operation type (`plan`, `apply`, `plan-destroy`, `plan-refresh-only`, `apply-destroy`, ...):

`terraform graph -type={{operation_type}}`

- Generate a graph based on a saved plan file:

`terraform graph -plan={{path/to/file.tfplan}}`

- Highlight cycles in the dependency graph (useful for debugging):

`terraform graph -draw-cycles`

- Render the graph as a PNG image using Graphviz:

`terraform graph | dot -Tpng -o {{path/to/graph.png}}`
