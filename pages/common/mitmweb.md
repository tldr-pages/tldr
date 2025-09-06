# mitmweb

> A web-based interactive man-in-the-middle HTTP proxy.
> See also: `mitmproxy`.
> More information: <https://docs.mitmproxy.org/stable/concepts-options>.

- Start `mitmweb` with default settings:

`mitmweb`

- Start `mitmweb` bound to a custom address and port:

`mitmweb --listen-host {{ip_address}} --listen-port {{port}}`

- Start `mitmweb` using a script to process traffic:

`mitmweb --scripts {{path/to/script.py}}`
