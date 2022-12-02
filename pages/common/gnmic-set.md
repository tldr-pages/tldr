# gnmic set

> Modify gnmi network device configuration.
> More information: <https://gnmic.kmrd.dev/cmd/set>.

- Update the value of a path:

`gnmic --address {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- Update the value of a path to match the contents of a json file:

`gnmic -a {{ip:port}} set --update-path {{path}} --update-file {{path/to/file}}`

- Replace the value of a path to match the contents of a json file:

`gnmic -a {{ip:port}} set --replace-path {{path}} --replace-file {{path/to/file}}`

- Delete the node at a given path:

`gnmic -a {{ip:port}} set --delete {{path}}`
