# mitmproxy

> An interactive man-in-the-middle HTTP proxy.
> See also: `mitmweb`.
> More information: <https://docs.mitmproxy.org/stable/concepts-options>.

- Start `mitmproxy` with default settings:

`mitmproxy`

- Start `mitmproxy` bound to a custom address and port:

`mitmproxy --listen-host {{ip_address}} --listen-port {{port}}`

- Start `mitmproxy` using a script to process traffic:

`mitmproxy --scripts {{path/to/script.py}}`
