# dolt pull

> Fetch from and integrate changes from a Dolt remote repository.
> See also: `dolt-fetch`, `dolt-push`.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-pull>.

- Fetch from the default remote and merge the changes into the current branch:

`dolt pull`

- Fetch from a specific remote and branch:

`dolt pull {{remote_name}} {{branch_name}}`

- Rebase the current branch on the remote changes instead of merging:

`dolt pull --rebase`
