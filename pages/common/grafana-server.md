# grafana server

> Start the Grafana web server.
> Run this from the Grafana installation directory, or specify `--homepath`.
> See also: `grafana`, `grafana-cli`.
> More information: <https://grafana.com/docs/grafana/latest/setup-grafana/start-restart-grafana/>.

- Start the Grafana server:

`grafana server`

- Start with a specific config file:

`grafana server --config {{path/to/grafana.ini}}`

- Start with a specific homepath (defaults to the working directory):

`grafana server --homepath {{path/to/grafana}}`

- Write the server process ID to a file:

`grafana server --pidfile {{path/to/file.pid}}`

- Override configuration options:

`grafana server --configOverrides {{cfg:default.paths.log=path/to/logfile}}`

- Print the current version along with all dependency versions:

`grafana server --vv`
