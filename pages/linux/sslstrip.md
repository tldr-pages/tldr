# sslstrip

> Perform Moxie Marlinspike's Secure Sockets Layer (SSL) stripping attacks with this Man-in-the-Middle (MITM) tool.
> More information: <https://www.kali.org/tools/sslstrip/>.

- Listen on a port:

`sslstrip --listen={{target_port}}`

- Log all SSL traffic to and from the server:

`sslstrip --ssl --listen={{target_port}}`

- Log all SSL and HTTP traffic to and from server:

`sslstrip --listen={{target_port}} --all`

- Specify output filename:

`sslstrip --listen={{target_port}} --write={{path/to/file}}`
