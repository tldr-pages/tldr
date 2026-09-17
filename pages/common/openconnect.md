# openconnect

> A VPN client, for Cisco AnyConnect VPNs and others.
> More information: <https://www.infradead.org/openconnect/manual.html>.

- Connect to a server:

`sudo openconnect {{vpn.example.org}}`

- Connect to a server, forking into the background:

`sudo openconnect {{[-b|--background]}} {{vpn.example.org}}`

- Terminate the connection that is running in the background:

`sudo killall -SIGINT openconnect`

- Specify the user to log in as:

`sudo openconnect {{[-u|--user]}} {{username}} {{vpn.example.org}}`

- Specify the connection protocol:

`sudo openconnect --protocol {{nc|pulse|gp|f5|fortinet|array}} {{vpn.example.org}}`

- Connect to a server, reading options from a configuration file:

`sudo openconnect --config {{path/to/config_file}} {{vpn.example.org}}`

- Connect to a server and authenticate with a specific SSL client certificate:

`sudo openconnect {{[-c|--certificate]}} {{path/to/certificate.pem}} {{vpn.example.org}}`
