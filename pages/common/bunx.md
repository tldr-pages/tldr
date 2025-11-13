# bunx

> Execute a package binary (installed locally or fetched remotely).
> Note: `bun x` can be used as an alias for `bunx`.
> More information: <https://bun.sh/docs/pm/bunx>.

- Download and execute a package from the registry:

`bunx {{package_name}} "{{command_argument}}"`

- Check the version of a locally installed package (if found):

`bunx {{package_name}} --version`

- Force an executable to run with the `Bun` runtime (instead of `Node`):

`bunx --bun {{package_name}}`

- Execute a binary that has a different name than its package:

`bunx {{[-p|--package]}} {{package_name}} {{command}}`

- Download and execute a specific version of a package:

`bunx {{package_name@version}} "{{command_argument}}"`
