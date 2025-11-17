# bun-info

> Display package metadata from the npm registry.
> More information: <https://bun.com/docs/pm/cli/info>.

- Display metadata for a package:

`bun info {{package_name}}`

- Display metadata for a specific version:

`bun info {{package_name}}@{{version}}`

- Show a specific property of a package:

`bun info {{package_name}} {{property}}`

- Output results in JSON format:

`bun info {{package_name}} --json`

- Display metadata for multiple packages:

`bun info {{package1}} {{package2}}`
