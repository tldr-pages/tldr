# openconnect

> A VPN client, for Cisco AnyConnect VPNs and others.
> More information: <https://www.infradead.org/openconnect/>

- Establish a VPN connection to the specified server:

`openconnect {{vpn.example.org}}`

- Establish a VPN connection to the specified server and continue in the background:

`openconnect --background {{vpn.example.org}}`

- Terminate a VPN session that is running in the background:

`killall -SIGINT openconnect`
