# mermaid-cli

> A command-line interface (CLI) for mermaid. It takes a mermaid definition file as input and generates svg/png/pdf file as output.
> More information: <https://mermaid-js.github.io/mermaid/>.

- Convert file to format speficied in file extension (svg|png|pdf):

`mmdc --input {{input.mmd}} --output {{output.svg}}`

- Change theme of the chart (forest|dark|neutral|default):

`mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{neutral}}`

- Change the background color of the chart (lime|"#D8064F"|transparent):

`mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}`
