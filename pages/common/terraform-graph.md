# terraform graph

> Generate a visual representation of configuration or execution plan.
> The output is in DOT format and can be rendered using GraphViz.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/graph>.

- Generate a dependency graph for the current configuration:

`terraform graph`

- Generate a graph and render it to a PNG file using GraphViz:

`terraform graph | dot -Tpng > {{path/to/graph.png}}`

- Generate a graph from a saved plan file:

`terraform graph -plan={{path/to/tfplan}}`

- Generate a graph highlighting dependency cycles:

`terraform graph -draw-cycles`

- Generate a graph of a specific type (plan, apply, etc.):

`terraform graph -type={{plan|plan-refresh-only|plan-destroy|apply}}`
