# chroma

> Chroma is a general-purpose syntax highlighting library and corresponding command, for Go.
> More information: <https://github.com/alecthomas/chroma>.

- Highlight a source file with Python lexer and output to terminal:

`chroma --lexer="{{python}}" {{source_file}}`

- Highlight a source file with the Go lexer and output to an HTML file:

`chroma --lexer="{{go}}" --formatter="{{html}}" {{source_file}} > {{html_file}}`

- Highlight a source file with the C++ lexer and output to an SVG, using the Monokai style:

`chroma --lexer="{{c++}}" --formatter="{{svg}}" --style="{{monokai}}" {{source_file}} > {{svg_file}}`
