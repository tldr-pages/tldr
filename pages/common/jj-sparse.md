# jj sparse

> Manage which paths from the working-copy commit are present in the working copy.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-sparse>.

- List the patterns currently present in the working copy:

`jj sparse list`

- Start an editor to update the sparse patterns:

`jj sparse edit`

- Reset the patterns to include all files in the working copy:

`jj sparse reset`

- Exclude all files from the working copy:

`jj sparse set --clear`

- Update patterns to only include specified paths:

`jj sparse set --clear --add {{path/to/directory}}`

- Add a path to the working copy:

`jj sparse set --add {{path/to/directory}}`

- Add multiple paths to the working copy:

`jj sparse set --add {{path/to/directory1}} --add {{path/to/directory2}}`

- Remove a path from the working copy:

`jj sparse set --remove {{path/to/directory}}`
