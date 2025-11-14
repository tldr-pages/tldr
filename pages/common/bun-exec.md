# bun exec

> Run a package’s binary without installing it globally.
> More information: <https://bun.sh/docs>.

- Run a binary from the npm registry:

`bun exec {{package_name}}`

- Run a binary and pass arguments to it:

`bun exec {{package_name}} {{arg1}} {{arg2}}`

- Run a specific version of a package:

`bun exec {{package_name}}@{{version}}`

- Run a local project’s binary:

`bun exec ./path/to/{{script.js}}`

- Use bun exec with npx-style behavior:

`bun exec -- {{command}} {{args}}`
