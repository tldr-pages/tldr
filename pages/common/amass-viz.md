# amass viz

> Visualize gathered information in a network graph.
> More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Generate a D3.js visualization based on database data:

`amass viz -d3 -dir {{path/to/database_directory}}`

- Generate a DOT file based on database data:

`amass viz -dot -dir {{path/to/database_directory}}`

- Generate a Gephi Graph Exchange XML Format (GEXF) file based on database data:

`amass viz -gexf -dir {{path/to/database_directory}}`

- Generate a Graphistry JSON file based on database data:

`amass viz -graphistry -dir {{path/to/database_directory}}`

- Generate a Maltego CSV file based on database data:

`amass viz -maltego -dir {{path/to/database_directory}}`
