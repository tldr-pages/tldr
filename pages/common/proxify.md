# proxify

> A versatile and portable proxy for capturing, manipulating, and replaying HTTP/HTTPS traffic on the go.
> See also: `mitmproxy`.
> More information: <https://github.com/projectdiscovery/proxify>.

- Start HTTP proxy (on default network interface `127.0.0.1` port `8888`):

`proxify`

- Start HTTP proxy on custom network interface and port (may require `sudo` for port number lower than `1024`):

`proxify -http-addr "{{network_interface}}:{{port_number}}"`

- Specify output format and file:

`proxify -output-format {{jsonl|yaml}} -output {{path/to/file}}`

