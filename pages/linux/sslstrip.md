# sslstrip

> The sslstrip is a tool that transparently hijacks HTTP traffic on a network.
> More information: <https://www.kali.org/tools/sslstrip/>.

- Listen to a port:

`sslstrip --listen={{target_port}}`

- Log all SSL traffic to and from server:

`sslstrip --ssl --listen={{target_port}}`

- Log all SSL and HTTP traffic to and from server:

`sslstrip --listen={{target_port}} --all`

- Specify output filename:

`sslstrip --listen={{target_port}} --write={{file_name}}`
