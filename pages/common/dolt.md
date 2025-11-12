# dolt

> An SQL database that you can fork, clone, branch, merge, push, and pull just like a Git repository.
> Some subcommands such as `commit` and `sql` have their own usage documentation.
> More information: <https://docs.dolthub.com/cli-reference/cli>.

- Initialize a new Dolt repository in the current directory:

`dolt init`

- Clone a Dolt repository from a remote source:

`dolt clone {{remote_repository_url}}`

- View the current repository status:

`dolt status`

- Commit staged changes with a message:

`dolt commit -m "{{commit_message}}"`

- Merge another branch into the current branch:

`dolt merge {{branch_name}}`

- List available subcommands:

`dolt help`

- Display version information:

`dolt --version`
