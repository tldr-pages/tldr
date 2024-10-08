# gpclient

> Client for using GlobalProtect VPN on Linux via OpenConnect.
> `gpclient` allows you to connect, disconnect, and manage VPN connections using a command-line interface or a graphical user interface (GUI).
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

- Print version information:

`gpclient --version`

- Print help for any command:

`gpclient help {{command}}`

---