# openconnect

> A VPN client, for Cisco AnyConnect VPNs and others.
> More information: <https://www.infradead.org/openconnect/manual.html>.

- Establish a VPN connection to the specified server:

`openconnect {{vpn.example.org}}`

- Connect to a server, forking into the background:

`openconnect --background {{vpn.example.org}}`

- Terminate a VPN session that is running in the background:

`killall -SIGINT openconnect`
