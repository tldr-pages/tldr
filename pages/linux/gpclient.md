# gpclient

> Connect to a GlobalProtect VPN on Linux via OpenConnect.
> More information: <https://github.com/yuezk/GlobalProtect-openconnect>.

- Connect to a GlobalProtect VPN using a portal server:

`gpclient connect {{vpn_gateway_url}}`

- Disconnect from the currently connected VPN server:

`gpclient disconnect`

- Launch the graphical user interface (GUI) for VPN management:

`gpclient launch-gui`

- Use OpenSSL workaround to bypass legacy renegotiation errors:

`gpclient connect --fix-openssl {{vpn_gateway_url}}`

- Ignore TLS errors during connection:

`gpclient connect --ignore-tls-errors {{vpn_gateway_url}}`

- Display version:

`gpclient --version`

- Display help for any command:

`gpclient help {{command}}`
