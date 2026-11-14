# grafana cli plugins

> Manage plugins for Grafana.
> More information: <https://grafana.com/docs/grafana/latest/administration/cli/#plugins-commands>.

- List all installed plugins:

`grafana cli plugins ls`

- List all available plugins from the remote repository:

`grafana cli plugins list-remote`

- List available versions for a specific plugin:

`grafana cli plugins list-versions {{plugin_id}}`

- Install a specific plugin:

`grafana cli plugins install {{plugin_id}}`

- Update all installed plugins:

`grafana cli plugins update-all`

- Update a specific plugin:

`grafana cli plugins update {{plugin_id}}`

- Remove a specific plugin:

`grafana cli plugins remove {{plugin_id}}`
