# chroma

> A general-purpose syntax highlighter.
> The `--lexer` option is usually unnecessary, as it will be automatically determined based on the file extension.
> More information: <https://github.com/alecthomas/chroma>.

- Highlight source code from a file with the Python lexer and output to `stdout`:

`chroma --lexer {{python}} {{path/to/source_file.py}}`

- Highlight source code from a file with the Go lexer and output to an HTML file:

`chroma --lexer {{go}} --formatter {{html}} {{path/to/source_file.go}} > {{path/to/target_file.html}}`

- Highlight source code from `stdin` with the C++ lexer and output to an SVG file, using the Monokai style:

`{{command}} | chroma --lexer {{c++}} --formatter {{svg}} --style {{monokai}} > {{path/to/target_file.svg}}`

- List available lexers, styles and formatters:

`chroma --list`
