# git alias

> Use to execute operation on multiple git repositories at a time.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-bulk>.

- Register a workspace (only absolute path):

`git bulk --addworkspace {{name}} {{path/to/workspace}}`

- Register the current directory as a workspace:

`git bulk --addcurrent {{name}}`

- Register a workspace with repository added from url:

`git bulk --addcurrent {{name}} {{path/to/workspace}} --from {{repository_url}}`

- List all registered workspaces:

`git bulk --listall`

- Run a git command on the specific workspace repositories:

`git bulk -w {{name}} {{git_command}}`

- Run a git command on all workspaces and their repositories:

`git bulk -a {{git_command}}`

- Remove a registered workspace:

`git bulk --removeworkspace {{name}}`

- Remove all registered workspaces:

`git bulk --purge`
