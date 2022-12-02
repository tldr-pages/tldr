# promtool

> Tooling for the Prometheus monitoring system.
> More information: <https://prometheus.io/docs/prometheus/latest/getting_started/>.

- Check if the config files are valid or not (if present report errors):

`promtool check config {{path/to/file.yml}}`

- Check if the rule files are valid or not (if present report errors):

`promtool check rules {{path/to/file.yml}}`

- Pass Prometheus metrics over `stdin` to check them for consistency and correctness:

`curl --silent {{http://example.com:9090/metrics/}} | promtool check metrics`

- Unit tests for rules config:

`promtool test rules {{path/to/file.yml}}`
