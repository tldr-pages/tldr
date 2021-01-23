# openfortivpn

> A VPN client, for Fortinet's proprietary PPP+SSL VPN solution.
> More information: <https://github.com/adrienverge/openfortivpn>.

- Connect to a VPN with a username and password:

`openfortivpn --username={{username}} --password={{password}}`

- Connect to a VPN using a specific configuration file (defaults to `/etc/openfortivpn/config`):

`sudo openfortivpn --config={{path/to/config}}`

- Connect to a VPN by specifying the host and port:

`openfortivpn {{host}}:{{port}}`

- Trust a given gateway by passing in its certificate's sha256 sum:

`openfortivpn --trusted-cert={{sha256_sum}}`
