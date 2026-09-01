# dolt push

> Push local commits to a Dolt remote.
> See also: `dolt-fetch`, `dolt-pull`.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-push>.

- Push the current branch to the default remote:

`dolt push`

- Push a specific branch to a specific remote:

`dolt push {{remote_name}} {{branch_name}}`

- Push the current branch and set its remote counterpart as upstream:

`dolt push {{[-u|--set-upstream]}} {{remote_name}} {{branch_name}}`

- Push a local branch to a differently named remote branch:

`dolt push {{remote_name}} {{local_branch}}:{{remote_branch}}`

- Delete a remote branch by pushing an empty source ref:

`dolt push {{remote_name}} :{{branch_name}}`
