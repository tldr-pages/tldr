# tree-sitter

> CLI tool for creating, testing, and using Tree-sitter parsers.
> Tree-sitter is a parser generator tool and incremental parsing library.
> More information: <https://tree-sitter.github.io/tree-sitter/cli/>.

- Initialize a new Tree-sitter parser project in the current directory:

`tree-sitter init`

- Generate parser source files from a `grammar.js`:

`tree-sitter generate`

- Parse a source file and print the syntax tree:

`tree-sitter parse {{path/to/source_file}}`

- Run the test suite for the parser:

`tree-sitter test`

- Run a specific test by name pattern:

`tree-sitter test --include '{{test_name_pattern}}'`

- Highlight a source file using the parser:

`tree-sitter highlight {{path/to/source_file}}`

- Run a query on source files and display matches:

`tree-sitter query {{path/to/query.scm}} {{path/to/source_file}}`

- Initialize the Tree-sitter CLI configuration file:

`tree-sitter init-config`
