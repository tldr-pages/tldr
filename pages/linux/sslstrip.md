# sslstrip

> Perform Moxie Marlinspike's SSL stripping attacks with this MITM tool.
> More information: <https://www.kali.org/tools/sslstrip/>.

- Listen on a port:

`sslstrip --listen={{target_port}}`

- Log all SSL traffic to and from server:

`sslstrip --ssl --listen={{target_port}}`

- Log all SSL and HTTP traffic to and from server:

`sslstrip --listen={{target_port}} --all`

- Specify output filename:

`sslstrip --listen={{target_port}} --write={{file_name}}`
