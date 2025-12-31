# miniserve

> Simple HTTP file server.
> More information: <https://github.com/svenstaro/miniserve#usage>.

- Serve a directory:

`miniserve {{path/to/directory}}`

- Serve a single file:

`miniserve {{path/to/file}}`

- Serve a directory using HTTP basic authentication:

`miniserve {{[-a|--auth]}} {{username}}:{{password}} {{path/to/directory}}`
