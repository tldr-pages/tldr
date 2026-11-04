# jj workspace

> Manage Jujutsu workspaces.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-workspace>.

- List all workspaces attached to the repository:

`jj workspace list`

- Create a new workspace at the specified path:

`jj workspace add {{path/to/directory}}`

- Create a new workspace with a specific name and parent revision:

`jj workspace add --name {{workspace_name}} {{[-r|--revision]}} {{revision}} {{path/to/directory}}`

- Print the root directory of the current workspace:

`jj workspace root`

- Print the root directory of a specific workspace:

`jj workspace root --name {{workspace_name}}`

- Rename the current workspace:

`jj workspace rename {{new_name}}`

- Stop tracking a workspace without deleting its files:

`jj workspace forget {{workspace_name}}`

- Update a workspace whose working copy has become stale:

`jj workspace update-stale`
