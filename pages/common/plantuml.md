# plantuml

> Create UML diagrams from a plain text language and render them in different formats.
> More information: <https://plantuml.com/en/command-line>.

- Render diagrams to default format (PNG):

`plantuml {{diagram1.puml}} {{diagram2.puml}}`

- Render a diagram in given format (e.g. `png`, `pdf`, `svg`, `txt`):

`plantuml -t{{format}} {{diagram.puml}}`

- Render all diagrams of a directory:

`plantuml {{path/to/diagrams}}`

- Render a diagram to the output directory:

`plantuml -o {{path/to/output}} {{diagram.puml}}`

- Render a diagram with the configuration file:

`plantuml -config {{config.cfg}} {{diagram.puml}}`

- Display help:

`plantuml -help`
