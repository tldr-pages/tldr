# mitmdump

> View, record, and programmatically transform HTTP traffic.
> The command-line counterpart to mitmproxy.
> More information: <https://docs.mitmproxy.org/stable/#mitmdump>.

- Start a proxy and save all output to a file:

`mitmdump {{[-w|--wfile]}} {{path/to/file}}`

- Filter a saved traffic file to just POST requests:

`mitmdump {{[-nr|--no-server --read-flows]}} {{input_filename}} {{[-w|--wfile]}} {{output_filename}} "{{~m post}}"`

- Replay a saved traffic file:

`mitmdump {{[-nc|--no-server --client-replay]}} {{path/to/file}}`

- Intercept DNS traffic (starts an intercepting DNS server on 127.0.0.1:53):

`sudo mitmdump {{[-m|--mode]}} dns`
