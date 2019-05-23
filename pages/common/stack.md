# stack

> Tool for managing Haskell projects.
> More information: <https://github.com/commercialhaskell/stack>.

- Create a new project:

`stack new {{project_name}}`

- Install all packages needed by a project:

`stack install`

- Compile a project:

`stack build`

- Run tests inside a project:

`stack test`

- Compile a project and re-compile every time a file changes:

`stack build --file-watch`

- Compile a project and execute a command after compilation:

`stack build --exec "{{command}}"`

- Run a program and pass an argument to it:

`stack exec {{program_name}} -- {{argument}}`
