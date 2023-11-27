# sg

> Ast-grep is a tool for code structural search, lint, and rewriting.
> More information: <https://ast-grep.github.io/guide/introduction.html>.

- Scan for possible queries using interactive mode:

`sg scan --interactive`

- Rewrite code in the current directory using patterns:

`sg run --pattern {{'foo'}} --rewrite {{'bar'}} --lang {{python}}`

- Visualize possible changes without applying them:

`sg -p 'useState<number>($A)' -r 'useState($A)' -l ts`

- JSON Mode:

`sg run -p 'Some($A)' -r 'None' --json | jq '.[].replacement' | jless`
