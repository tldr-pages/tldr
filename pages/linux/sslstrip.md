# sslstrip

> Perform Moxie Marlinspike's Secure Sockets Layer (SSL) stripping attacks. Perform an ARP spoofing before using this tool.
> More information: <https://www.kali.org/tools/sslstrip/>.

- Listen on a specific port:

`sslstrip --listen={{target_port}}`

- Log all SSL traffic to and from the server:

`sslstrip --ssl --listen={{target_port}}`

- Log all SSL and HTTP traffic to and from the server:

`sslstrip --listen={{target_port}} --all`

- Specify the file path to store the logs:

`sslstrip --listen={{target_port}} --write={{path/to/file}}`

- Display help:

`sslstrip --help`
