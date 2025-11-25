# gnmic

> A gNMI client.
> Manage gNMI network device configuration and view operational data.
> More information: <https://gnmic.openconfig.net/user_guide/configuration_flags/>.

- Request device capabilities:

`gnmic {{[-a|--address]}} {{ip:port}} capabilities`

- Provide a username and password to fetch device capabilities:

`gnmic {{[-a|--address]}} {{ip:port}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} capabilities`

- Get a snapshot of the device state at a specific path:

`gnmic {{[-a|--address]}} {{ip:port}} get --path {{path}}`

- Update device state at a specific path:

`gnmic {{[-a|--address]}} {{ip:port}} set --update-path {{path}} --update-value {{value}}`

- Subscribe to target state updates under the subtree at a specific path:

`gnmic {{[-a|--address]}} {{ip:port}} subscribe --path {{path}}`
