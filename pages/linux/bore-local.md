# bore local

> Start a local proxy to a remote server using Bore.
> More information: <https://github.com/ekzhang/bore#detailed-usage>.

- Expose a local port to a remote Bore server:

`bore local {{[-t|--to]}} {{remote_server_address}} {{local_port}}`

- Expose a specific local host instead of `localhost`:

`bore local {{[-l|--local-host]}} {{host}} {{[-t|--to]}} {{remote_server_address}} {{local_port}}`

- Specify a remote server port explicitly:

`bore local {{[-t|--to]}} {{remote_server_address}} {{[-p|--port]}} {{remote_port}} {{local_port}}`

- Use a secret for authentication:

`bore local {{[-t|--to]}} {{remote_server_address}} {{[-s|--secret]}} {{your_secret}} {{local_port}}`

- Display help:

`bore local {{[-h|--help]}}`
