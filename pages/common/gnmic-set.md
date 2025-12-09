# gnmic set

> Modify gnmi network device configuration.
> More information: <https://gnmic.kmrd.dev/cmd/set>.

- Update the value of a path:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{path/to/directory}} --update-value {{value}}`

- Update the value of a path to match the contents of a JSON file:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{path/to/directory}} --update-file {{path/to/file}}`

- Replace the value of a path to match the contents of a JSON file:

`gnmic {{[-a|--address]}} {{ip:port}} set --replace-path {{path/to/directory}} --replace-file {{path/to/file}}`

- Delete the node at a given path:

`gnmic {{[-a|--address]}} {{ip:port}} set --delete {{path/to/directory}}`
