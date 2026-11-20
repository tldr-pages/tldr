# gnmic set

> Modify gnmi network device configuration.
> More information: <https://gnmic.openconfig.net/cmd/set/>.

- Update the value of a path:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{gNMI_path}} --update-value {{value}}`

- Update the value of a path to match the contents of a JSON file:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{gNMI_path}} --update-file {{path/to/file}}`

- Replace the value of a path to match the contents of a JSON file:

`gnmic {{[-a|--address]}} {{ip:port}} set --replace-path {{gNMI_path}} --replace-file {{path/to/file}}`

- Delete the node at a given path:

`gnmic {{[-a|--address]}} {{ip:port}} set --delete {{gNMI_path}}`
