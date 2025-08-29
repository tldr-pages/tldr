# bore local

> Starts a local proxy to a remote server using Bore.
> More information: <https://github.com/ekzhang/bore>.

- Expose a local port to a remote Bore server:

`bore local --to {{remote_server_address}} {{local_port}}`

- Expose a specific local host instead of `localhost`:

`bore local --local-host {{host}} --to {{remote_server_address}} {{local_port}}`

- Specify a remote server port explicitly:

`bore local --to {{remote_server_address}} --port {{remote_port}} {{local_port}}`

- Use a secret for authentication:

`bore local --to {{remote_server_address}} --secret {{your_secret}} {{local_port}}`

- Display help:

`bore local --help`
