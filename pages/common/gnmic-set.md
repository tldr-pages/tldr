# gnmic set

> It is used to send a Set Request to the specified target(s) and expects one Set Response per target.
> Set RPC allows the client to modify the state of data on the target. The data specified referenced by a path can be updated, replaced or deleted.
> More information: <https://gnmic.kmrd.dev/cmd/set>.

- Update the value of a path:

`gnmic -a {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- Update the value of a path to match the contents of a json file:

`gnmic -a {{ip:port}} set --update-path {{path}} --update-file {{filepath}}`

- Replace the value of a path to match the contents of a json file:

`gnmic -a {{ip:port}} set --replace-path {{path}} --replace-file {{filepath}}`

- Delete the node at a given path:

`gnmic -a {{ip:port}} set --delete {{path}}`
