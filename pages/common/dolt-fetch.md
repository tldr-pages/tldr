# dolt fetch

> Download objects and refs from another repository.
> More information: <https://docs.dolthub.com/cli-reference/cli#dolt-fetch>.

- Fetch the latest changes from the default remote upstream repository (origin):

`dolt fetch`

- Fetch latest changes from a specific remote upstream repository:

`dolt fetch {{remote_name}}`

- Update branches with the current state of the remote, overwriting any conflicting history:

`dolt fetch -f`
