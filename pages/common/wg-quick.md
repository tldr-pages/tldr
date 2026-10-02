# wg-quick

> Quickly set up WireGuard tunnels based on config files.
> More information: <https://manned.org/wg-quick>.

- Set up a VPN tunnel based on `/etc/wireguard/interface.conf`:

`sudo wg-quick up {{interface}}`

- Delete a VPN tunnel:

`sudo wg-quick down {{interface}}`

- Save the current config of a tunnel to `/etc/wireguard/interface.conf`:

`sudo wg-quick save {{interface}}`

- Print the config of a tunnel with `wg-quick`-specific options removed:

`sudo wg-quick strip {{interface}}`
