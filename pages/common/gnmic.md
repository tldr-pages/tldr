# gnmic

> A gNMI command-line client.
> Manage gNMI network device configuration and view operational data.
> More information: <https://gnmic.kmrd.dev>.

- Request device capabilities:

`gnmic --address {{ip:port}} --insecure capabilities`

- Provide a username and password to fetch device capabilities:

`gnmic --address {{ip:port}} --username {{username}} --password {{password}} --insecure capabilities`

- Get a snapshot of the device state at {{path}}:

`gnmic -a {{ip:port}} --insecure get --path {{path}}`

- Update device state at {{path}}:

`gnmic -a {{ip:port}} --insecure set --update-path {{path}} --update-value {{value}}`

- Subscribe to target state updates under the subtree {{path}}:

`gnmic -a {{ip:port}} --insecure subscribe --path {{path}}`
