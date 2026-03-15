# sg

> A tool for code structural search, lint, and rewriting based on abstract syntax trees.
> Some subcommands such as `sg run`, `sg scan`, and `sg new` have their own usage documentation.
> More information: <https://ast-grep.github.io>.

- Search for a pattern in the current directory:

`sg run --pattern '{{console.log($ARG)}}' --lang {{javascript}}`

- Replace a pattern with a new string:

`sg run --pattern '{{var $NAME = $VALUE}}' --rewrite '{{let $NAME = $VALUE}}' --lang {{javascript}}`

- Scan the codebase using configured rules interactively:

`sg scan --interactive`

- Scan the codebase with a single rule file:

`sg scan --rule {{path/to/rule.yml}}`

- Create a new ast-grep project:

`sg new project`

- Test ast-grep rules:

`sg test`

- Start the language server:

`sg lsp`
