# grafana cli

> Administer Grafana plugins and related CLI options.
> See also: `grafana cli admin`.
> More information: <https://grafana.com/docs/grafana/latest/administration/cli/>.

- Install plugins:

`grafana cli plugins install {{plugin_id1 plugin_id2 ...}}`

- Install a plugin using a specific Grafana home directory:

`grafana cli --homepath {{/usr/share/grafana}} plugins install {{plugin_id}}`

- List plugins available from the remote repository:

`grafana cli plugins list-remote`

- List all installed plugins:

`grafana cli plugins ls`

- Update one or more plugins:

`grafana cli plugins update {{plugin_id1 plugin_id2 ...}}`

- Update all installed plugins:

`grafana cli plugins update-all`

- Remove plugins:

`grafana cli plugins remove {{plugin_id1 plugin_id2 ...}}`

- Display help:

`grafana cli {{[-h|--help]}}`
