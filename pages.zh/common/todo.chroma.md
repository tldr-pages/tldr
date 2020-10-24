# chroma

> Chroma is a general-purpose syntax highlighting library and corresponding command, for Go.
> More information: <https://github.com/alecthomas/chroma>.

- Highlight a source file with python lexer and output to terminal:

`chroma --lexer="{{python}}" {{source_file}}`

- Highlight a source file with Go lexer and output to a HTML file:

`chroma --lexer="{{go}}" --formatter="{{html}}" {{source_file}} > {{html_file}}`

- Highlight a source file with C++ lexer and output to an SVG image, using the Monokai style:

`chroma --lexer="{{c++}}" --formatter="{{svg}}" --syle="{{monokai}}" {{source_file}} > {{svg_file}}`
