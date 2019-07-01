# mitmdump

> View, record, and programmatically transform HTTP traffic.
> The command-line counterpart to mitmproxy.
> More information: <https://docs.mitmproxy.org/stable/overview-tools/#mitmdump>.

- Start a proxy and save all output to a file:

`mitmdump -w {{filename}}`

- Filter a saved traffic file to just POST requests:

`mitmdump -nr {{input_filename}} -w {{output_filename}} {{"~m post"}}`

- Replay a saved traffic file:

`mitmdump -nc {{filename}}`
