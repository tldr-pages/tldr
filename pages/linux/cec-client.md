# cec-client

> Manage CEC connections.
> More information: <https://manned.org/man/cec-client>.

- List all CEC adapters:

`cec-client {{[-l|--list-devices]}}`

- Start an interactive CEC session:

`cec-client`

- Set the On-Screen Display name:

`cec-client {{[-o|--osd-name]}} {{name}}`

- Send a single command:

`echo {{on 0}} | cec-client {{[-s|--single-command]}}`

- Set a device to standby in interactive mode:

`standby 0`

- Turn a device on in interactive mode:

`on 0`
