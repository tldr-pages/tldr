# grafana cli

> Administer Grafana.
> More information: <https://grafana.com/docs/grafana/latest/administration/cli/>.

- Install plugins:

`grafana cli plugins install {{plugin_id1 plugin_id2 ...}}`

- Specify a homepath when installing a plugin:

`grafana cli --homepath {{/usr/share/grafana}} plugins install {{plugin_id}}`

- Update plugins:

`grafana cli plugins update {{plugin_id1 plugin_id2 ...}}`

- Remove plugins:

`grafana cli plugins remove {{plugin_id1 plugin_id2 ...}}`

- List all installed plugins:

`grafana cli plugins ls`
