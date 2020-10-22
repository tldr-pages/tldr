# openconnect

> A VPN client, for Cisco AnyConnect VPNs and others.
> More information: <https://www.infradead.org/openconnect/manual.html>.

- Connect to a server:

`openconnect {{vpn.example.org}}`

- Connect to a server, forking into the background:

`openconnect --background {{vpn.example.org}}`

- Terminate the connection that is running in the background:

`killall -SIGINT openconnect`
