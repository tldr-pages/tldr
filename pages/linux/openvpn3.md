# openvpn3

> OpenVPN 3 Linux client.
> More information: <https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux>.

- Start a new VPN session:

`openvpn3 session-start {{[-c|--config]}} {{path/to/config.conf}}`

- List established sessions:

`openvpn3 sessions-list`

- Disconnect the currently established session started with given configuration:

`openvpn3 session-manage {{[-c|--config]}} {{path/to/config.conf}} {{[-D|--disconnect]}}`

- Import VPN configuration:

`openvpn3 config-import {{[-c|--config]}} {{path/to/config.conf}}`

- List imported configurations:

`openvpn3 configs-list`
