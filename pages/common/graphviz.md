# graphviz

> Open-source graph visualization software.
> More information: <https://graphviz.gitlab.io/>.

- Render a DOT file to a PNG image:

`dot -Tpng {{input.dot}} -o {{output.png}}`

- Convert a DOT file to an SVG:

`dot -Tsvg {{input.dot}} -o {{output.svg}}`

- Display a Graphviz file as an SVG in a browser:

`dot -Tsvg {{input.dot}} | xdg-open -`

- Generate a PDF from a DOT file:

`dot -Tpdf {{input.dot}} -o {{output.pdf}}`

- Render a DOT file to ASCII art:

`dot -Tplain {{input.dot}}`

- Preview a DOT graph in a Mac viewer:

`dot -Tpdf {{input.dot}} | open -f -a Preview`

- List available Graphviz output formats:

`dot -T? {{input.dot}}`

- Show Graphviz version:

`dot -V`
