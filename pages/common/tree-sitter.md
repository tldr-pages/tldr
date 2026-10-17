# tree-sitter

> Incremental parser generator and syntax tree library.
> Some subcommands such as `generate` or `parse` have their own usage documentation.
> More information: <https://tree-sitter.github.io/tree-sitter/>.

- Initialize a new Tree-sitter grammar in the current directory:

`tree-sitter init`

- Generate C parser code from the grammar:

`tree-sitter generate`

- Compile the generated parser into a dynamic library:

`tree-sitter build`

- Run corpus parser tests for the grammar:

`tree-sitter test`

- Parse one or more source files and display the syntax tree:

`tree-sitter parse {{path/to/file}}`

- Highlight a source file using syntax queries:

`tree-sitter highlight {{path/to/file}}`

- Start an interactive web playground in a browser:

`tree-sitter playground`

- Execute a syntax query against one or more source files:

`tree-sitter query {{path/to/query.scm}} {{path/to/file}}`
