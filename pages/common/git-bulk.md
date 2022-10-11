# git bulk

> Execute operations on multiple git repositories.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Register a new workspace into git-bulk:

`git bulk --addworkspace {{workspace_name}} {{absolute/path/to/root/directory}}`

- Register a new workspace and a git repository attached to it:

`git bulk --addworkspace {{workspace-name}} {{absolute/path/to/root/directory}} --from {{git_repo_url}}`

- Register a new workspace and attach some git repositories from a file:

`git bulk --addworkspace {{workspace-name}} {{absolute/path/to/root/directory}} --from {{absolute/path/to/file}}`

- List all registered workspaces:

`git bulk --listall`

- Run a git command on the repositories of the current workspace:

`git bulk {{git_command}}`
