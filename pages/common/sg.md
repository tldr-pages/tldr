# sg

> Ast-grep is a tool for code structural search, lint, and rewriting.
> More information: <https://ast-grep.github.io/guide/introduction.html>.

- Scan possible queries on interactive mode:

`sg scan --interactive`

- Rewrite code using patterns on current directory:

`sg run --pattern {{'foo'}} --rewrite {{'bar'}} --lang {{python}}`

- Visualize possible changes without applying them:

`sg -p 'useState<number>($A)' -r 'useState($A)' -l ts`

- JSON Mode:

`sg run -p 'Some($A)' -r 'None' --json | jq '.[].replacement' | jless`
