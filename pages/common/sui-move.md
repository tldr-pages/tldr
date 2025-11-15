# sui move

> Work with Move source code.
> More information: <https://docs.sui.io/references/cli/move>.

- Create a new Move project in the given folder:

`sui move new {{project_name}}`

- Test the Move project in the current directory:

`sui move test`

- Test with coverage and get a summary:

`sui move test --coverage; sui move coverage summary`

- Find which parts of your code are covered from tests (i.e. explain coverage results):

`sui move coverage source --module {{module_name}}`

- Build the Move project in the current directory:

`sui move build`

- Build the Move project from the given path:

`sui move build --path {{path}}`

- Migrate to Move 2024 for the package at the provided path:

`sui move migrate {{path}}`
