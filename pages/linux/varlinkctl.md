# varlinkctl

> Control and interact with Varlink services.
> More information: <https://www.freedesktop.org/software/systemd/man/varlinkctl.html>.

- List available Varlink services:

`varlinkctl list`

- Show information about a specific service:

`varlinkctl info {{service}}`

- Call a method on a service:

`varlinkctl call {{service}} {{method}}`

- Call a method with JSON arguments:

`varlinkctl call {{service}} {{method}} '{{{"key": "value"}}}'`

- Monitor a service:

`varlinkctl monitor {{service}}`
