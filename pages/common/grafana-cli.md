# grafana cli

> Administer Grafana.
> More information: <https://grafana.com/docs/grafana/latest/administration/cli/>.

- Display help:

`grafana cli --help`

- Display the version:

`grafana cli --version`

- Install one or more plugins:

`grafana cli plugins install {{plugin_id1 plugin_id2 ...}}`

- Install a plugin using a custom plugin directory:

`grafana cli --pluginsDir {{path/to/plugins_directory}} plugins install {{plugin_id}}`

- List all installed plugins:

`grafana cli plugins ls`

- Reset the admin password:

`grafana cli admin reset-admin-password {{new_password}}`
