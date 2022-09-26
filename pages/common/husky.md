# husky

> Native Git hooks made easy.
> More information: <https://typicode.github.io/husky>.

- Install Husky in the current directory:

`husky install`

- Install Husky into a specific directory:

`husky install {{path/to/directory}}`

- Set a specific command as a `pre-push` hook for Git:

`husky set {{.husky/pre-push}} "{{command}} {{command_arguments}}"`

- Add a specific command to the current `pre-commit` hook:

`husky add {{.husky/pre-commit}} "{{command}} {{command_arguments}}"`

- Uninstall Husky hooks from the current directory:

`husky uninstall`

- Display help:

`husky`
