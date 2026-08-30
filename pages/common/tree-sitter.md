# tree-sitter

> An incremental parsing system for programming tools.
> More information: <https://tree-sitter.github.io/tree-sitter/>.

- Generate a parser from `grammar.js`:

`tree-sitter generate`

- Parse a source file and print the syntax tree:

`tree-sitter parse {{path/to/file}}`

- Run parser unit tests located in `test/corpus`:

`tree-sitter test`

- Syntax highlight a source file in the terminal:

`tree-sitter highlight {{path/to/file}}`

- Initialize a default Tree-sitter configuration file:

`tree-sitter init-config`

- Build the parser library:

`tree-sitter build`
