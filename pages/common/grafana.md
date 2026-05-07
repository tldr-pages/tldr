# grafana

> Grafana server and command-line interface for managing the Grafana instance and its plugins.
> Some subcommands such as `cli` have their own usage documentation.
> More information: <https://grafana.com/docs/grafana/latest/cli/>.

- Start the Grafana server in the foreground:

`grafana server`

- Start the Grafana server with a specific configuration file:

`grafana server --config {{path/to/grafana.ini}}`

- Start the Grafana server with a specific home path (containing the `conf`, `public`, and `data` directories):

`grafana server --homepath {{path/to/grafana_home}}`

- Run a `grafana cli` subcommand (e.g. install a plugin):

`grafana cli plugins install {{plugin_id}}`

- Reset the admin user's password:

`grafana cli admin reset-admin-password {{new_password}}`

- Display the Grafana server version:

`grafana --version`

- Display help:

`grafana --help`
