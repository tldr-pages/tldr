# bun link

> Register a local package as linkable or link a registered package into a project.
> See also: `bun unlink`.
> More information: <https://bun.com/docs/pm/cli/link>.

- Link the current package globally:

`bun link`

- Link a package locally to a project:

`bun link {{package_name}}`

- Link a package in a specific directory:

`bun link --cwd {{path/to/package}}`

- Perform a dry run without actually linking:

`bun link --dry-run`

- Display help:

`bun link {{[-h|--help]}}`
