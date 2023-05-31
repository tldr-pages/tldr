# mitmproxy

> An interactive man-in-the-middle HTTP proxy.
> More information: <https://mitmproxy.org>.

- Start mitmproxy with default settings:

`mitmproxy`

- Start mitmproxy bound to custom address and port:

`mitmproxy -b {{ip_address}} -p {{port}}`

- Export the logs with SSL/TLS master keys, to external programs (wireshark,...)

`SSLKEYLOGFILE="{{path/to/file}}" mitmproxy`
