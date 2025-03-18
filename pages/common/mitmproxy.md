# mitmproxy

> An interactive man-in-the-middle HTTP proxy.
> See also: `mitmweb` and `mitmdump`.
> More information: <https://docs.mitmproxy.org/stable/>.

- Start `mitmproxy` with default settings (will listen on port `8080`):

`mitmproxy`

- Start `mitmproxy` bound to a custom address and port:

`mitmproxy --listen-host {{ip_address}} {{[-p|--listen-port]}} {{port}}`

- Start `mitmproxy` using a script to process traffic:

`mitmproxy {{[-s|--scripts]}} {{path/to/script.py}}`

- Export the logs with SSL/TLS master keys to external programs (wireshark, etc.):

`SSLKEYLOGFILE="{{path/to/file}}" mitmproxy`

- Specify mode of operation of the proxy server (`regular` is the default):

`mitmproxy {{[-m|--mode]}} {{regular|transparent|socks5|...}}`

- Set the console layout:

`mitmproxy --console-layout {{horizontal|single|vertical}}`
