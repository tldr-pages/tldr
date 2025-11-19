# bun patch

> Prepare a package for patching or generate a patch file.
> More information: <https://bun.com/docs/pm/cli/patch>.

- Prepare a package for patching:

`bun patch {{package}}`

- Prepare a specific version of a package:

`bun patch {{package}}@{{version}}`

- Prepare a package located at a path:

`bun patch {{path/to/package}}`

- Generate a patch file for changes made to a package:

`bun patch --commit {{node_modules/path/to/package}}`

- Generate a patch file and store it in a custom directory:

`bun patch --commit {{node_modules/path/to/package}} --patches-dir {{directory}}`
