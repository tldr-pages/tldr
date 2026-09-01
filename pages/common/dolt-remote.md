# dolt remote

> Manage the set of tracked Dolt remote repositories.
> See also: `dolt-fetch`, `dolt-pull`, `dolt-push`.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-remote>.

- List existing remotes:

`dolt remote`

- List remotes verbosely, including their URLs:

`dolt remote {{[-v|--verbose]}}`

- Add a remote:

`dolt remote add {{remote_name}} {{url}}`

- Remove a remote:

`dolt remote remove {{remote_name}}`
