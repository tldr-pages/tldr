# dolt fetch

> Download objects and refs from another repository.
> More information: <https://github.com/dolthub/dolt>.

- Fetch refs and update remote-tracking branches from the default remote named "origin":

`dolt fetch`

- Fetch refs and update remote-tracking branches from a specific remote:

`dolt fetch {{remote_name}}`

- Update refs to remote branches with the current state of the remote, overwriting any conflicting history:

`dolt fetch -f`
