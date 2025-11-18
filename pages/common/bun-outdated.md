# bun outdated

> Show dependencies that have newer versions available.
> More information: <https://bun.com/docs/pm/cli/outdated>.

- List all outdated dependencies in the current project:

`bun outdated`

- Check if a specific package is outdated:

`bun outdated {{package}}`

- List outdated dependencies matching a glob pattern:

`bun outdated "{{pattern}}"`

- Show outdated dependencies for specific workspaces:

`bun outdated --filter "{{workspace_pattern}}"`

- Recursively check all workspaces in a monorepo:

`bun outdated --recursive`
