# mmdc

> CLI for mermaid, a diagram generation tool with a domain-specific language.
> A mermaid definition file is taken as input and a SVG, PNG, or PDF file is generated as output.
> More information: <https://mermaid-js.github.io/mermaid/>.

- Convert a file to the specified format (automatically determined from the file extension):

`mmdc --input {{input.mmd}} --output {{output.svg}}`

- Specify the theme of the chart:

`mmdc --input {{input.mmd}} --output {{output.svg}} --theme {{forest|dark|neutral|default}}`

- Specify the background color of the chart (e.g. `lime`, `"#D8064F"`, or `transparent`):

`mmdc --input {{input.mmd}} --output {{output.svg}} --backgroundColor {{color}}`
