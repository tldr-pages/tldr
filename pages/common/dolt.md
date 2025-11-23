# dolt

> An SQL database that you can fork, clone, branch, merge, push, and pull just like a Git repository.
> Some subcommands such as `commit` have their own usage documentation.
> More information: <https://docs.dolthub.com/cli-reference/cli>.

- Initialize a new Dolt data repository:

`dolt init`

- Show the current working tree status:

`dolt status`

- Add a remote Dolt repository:

`dolt remote add {{repository_name}} {{url}}`

- Stage changes to tables:

`dolt add {{table_name}}`

- Record staged changes to the repository:

`dolt commit {{[-m|--message]}} "{{commit_message}}"`

- Push local changes to a remote:

`dolt push`

- Pull changes from a remote:

`dolt pull`
