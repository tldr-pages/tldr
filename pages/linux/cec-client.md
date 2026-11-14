# cec-client

> Manage serial bus CEC connections.
> See also: `cec-ctl`.
> More information: <https://manned.org/cec-client>.

- List all CEC adapters:

`cec-client {{[-l|--list-devices]}}`

- Start an interactive CEC session:

`sudo cec-client`

- Set the On-Screen Display name:

`sudo cec-client {{[-o|--osd-name]}} {{name}}`

- Send a single command:

`echo {{on 0}} | sudo cec-client {{[-s|--single-command]}}`

- [Interactive] Set a device to standby:

`standby {{0}}`

- [Interactive] Turn a device on:

`on {{0}}`
