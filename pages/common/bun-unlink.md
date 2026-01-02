# bun unlink

> Unregister the current directory as a linkable package.
> See also: `bun link`.
> More information: <https://bun.com/docs/pm/cli/link#unlinking>.

- Unregister the current package globally:

`bun unlink`

- Unregister a package in a specific directory:

`bun unlink --cwd {{path/to/package}}`

- Perform a dry run without actually unregistering:

`bun unlink --dry-run`

- Display help:

`bun unlink {{[-h|--help]}}`
