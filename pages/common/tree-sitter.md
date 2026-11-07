# tree-sitter

> Parser generator tool and an incremental parsing library.
> More information: <https://tree-sitter.github.io/tree-sitter/cli/>.

- Initialize a new grammar in the current directory:

`tree-sitter init`

- Generate the parser source code from `grammar.js`:

`tree-sitter generate`

- Compile the parser into a shared library:

`tree-sitter build`

- Parse a file and print the resulting syntax tree:

`tree-sitter parse {{path/to/source_file}}`

- Run the parser's test suite:

`tree-sitter test`

- Highlight a source file in the terminal:

`tree-sitter highlight {{path/to/source_file}}`

- Run a query file against a source file:

`tree-sitter query {{path/to/query.scm}} {{path/to/source_file}}`

- Display version:

`tree-sitter version`
