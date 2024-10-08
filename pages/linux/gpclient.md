# gpclient

> Client for using GlobalProtect VPN on Linux via OpenConnect.
> More information: <https://github.com/yuezk/GlobalProtect-openconnect>.

- Connect to a GlobalProtect VPN using a portal server:

`gpclient connect --portal {{vpn_gateway_url}}`

- Disconnect from the currently connected VPN server:

`gpclient disconnect`

- Launch the graphical user interface (GUI) for GlobalProtect VPN management:

`gpclient launch-gui`

- Bypass the OpenSSL `unsafe legacy renegotiation` error during connection:

`gpclient connect --fix-openssl --portal {{vpn_gateway_url}}`

- Ignore TLS errors during the connection process:

`gpclient connect --ignore-tls-errors --portal {{vpn_gateway_url}}`

- Print general help or detailed help for a specific command:

`gpclient help {{command}}`

- Display the version of the `gpclient` tool:

`gpclient --version`
