# proxify

> A versatile and portable proxy for capturing, manipulating, and replaying HTTP/HTTPS traffic on the go.
> See also: `mitmproxy`.
> More information: <https://github.com/projectdiscovery/proxify#usage>.

- Start a HTTP proxy (on the loopback network interface `127.0.0.1` and port `8888`):

`proxify`

- Start a HTTP proxy on a custom network interface and port (may require `sudo` for a port number lower than `1024`):

`proxify {{[-ha|-http-addr]}} "{{ip_address}}:{{port_number}}"`

- Specify output format and output file:

`proxify {{[-of|-output-format]}} {{jsonl|yaml}} {{[-o|-output]}} {{path/to/file}}`

- Display help:

`proxify -h`
