# influx

> InfluxDB command-line client.
> More information: <https://docs.influxdata.com/influxdb/v1.7/tools/shell/>.

- Connect to an InfluxDB running on localhost with no credentials:

`influx`

- Connect with a specific username (will prompt for a password):

`influx -username {{username}} -password ""`

- Connect to a specific host:

`influx -host {{hostname}}`

- Use a specific database:

`influx -database {{database_name}}`

- Execute a given command:

`influx -execute "{{influxql_command}}"`

- Return output in a specific format:

`influx -execute "{{influxql_command}}" -format {{json|csv|column}}`
