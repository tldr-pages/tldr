# bun update

> Update dependencies in a Bun project.
> More information: <https://bun.com/docs/pm/cli/update>.

- Update all dependencies:

`bun update`

- Update to the latest version, regardless of its compatibility:

`bun update --latest`

- Update a specific dependency:

`bun update {{package_name}}`

- Update a dependency to a specific version:

`bun update {{package_name}}@{{version}}`

- Update packages interactively:

`bun update {{[-i|--interactive]}}`

- Update dependencies recursively across all workspaces:

`bun update {{[-r|--recursive]}}`

- Update dependencies interactively and recursively:

`bun update {{[-i|--interactive]}} {{[-r|--recursive]}}`
