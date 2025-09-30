# dvc fetch

> Download DVC tracked files and directories from a remote repository.
> More information: <https://dvc.org/doc/command-reference/fetch>.

- Fetch the latest changes from the default remote upstream repository (if set):

`dvc fetch`

- Fetch changes from a specific remote upstream repository:

`dvc fetch {{[-r|--remote]}} {{remote_name}}`

- Fetch the latest changes for a specific target/s:

`dvc fetch {{target/s}}`

- Fetch changes for all branch and tags:

`dvc fetch {{[-a|--all-branches]}} {{[-T|--all-tags]}}`

- Fetch changes for all commits:

`dvc fetch {{[-A|--all-commits]}}`
