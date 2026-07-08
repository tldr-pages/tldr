# grafana cli admin

> Manage Grafana administrator commands.
> More information: <https://grafana.com/docs/grafana/latest/administration/cli/>.

- Show all admin commands:

`grafana cli admin`

- Reset the admin password:

`grafana cli admin reset-admin-password {{new_password}}`

- Reset the password for a specific user:

`grafana cli admin reset-admin-password --user-id {{user_id}} {{new_password}}`

- Reset the password using a specific Grafana home directory:

`grafana cli --homepath {{path/to/grafana}} admin reset-admin-password {{new_password}}`

- Display help:

`grafana cli admin {{[-h|--help]}}`

- Display version:

`grafana cli admin {{[-v|--version]}}`
