# mitmdump

> View, record, and programmatically transform HTTP traffic.
> The command-line counterpart to mitmproxy.
> More information: <https://docs.mitmproxy.org/stable/overview-tools/#mitmdump>.

- Start a proxy and save all output to a file:

`mitmdump -w {{path/to/file}}`

- Filter a saved traffic file to just POST requests:

`mitmdump -nr {{path/to/file}} -w {{path/to/file}} "{{~m post}}"`

- Replay a saved traffic file:

`mitmdump -nc {{path/to/file}}`
