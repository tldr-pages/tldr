# openfortivpn

> A VPN client, for Fortinet's proprietary PPP+SSL VPN solution.
> More information: <https://manned.org/openfortivpn>.

- Connect to a VPN with a username and password:

`openfortivpn {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Connect to a VPN using a specific configuration file (defaults to `/etc/openfortivpn/config`):

`sudo openfortivpn {{[-c|--config]}} {{path/to/config}}`

- Connect to a VPN by specifying the host and port:

`openfortivpn {{host}}:{{port}}`

- Trust a given gateway by passing in its certificate's sha256 sum:

`openfortivpn --trusted-cert {{sha256_sum}}`
