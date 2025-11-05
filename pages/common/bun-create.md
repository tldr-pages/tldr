# bun create

> Create a new project from a template.
> Note: `c` can be used as an alias for `create`.
> More information: <https://bun.com/docs/runtime/templating/create>.

- Create a new project from an official template interactively:

`bun create {{template}}`

- Create a new project from an official template in a new directory:

`bun create {{template}} {{path/to/destination}}`

- Create a new project from a GitHub repository template:

`bun create {{https://github.com/username/repo}} {{path/to/destination}}`

- Create a new project from a local template:

`bun create {{./path/to/template}} {{path/to/destination}}`

- Create a new project, overwriting the destination directory if it exists:

`bun create {{template}} {{path/to/destination} --force`

- Create a new project without initializing a Git repository automatically:

`bun create {{template}} {{path/to/destination} --no-git`

- Create a new project without installing dependencies automatically:

`bun create {{template}} {{path/to/destination} --no-install`
