# miniserve

> Simple HTTP file server CLI.
> For when you really just want to serve some files over HTTP right now!.
> More information: <https://github.com/svenstaro/miniserve>.

- Serve a directory:

`miniserve {{path/to/directory}}`

- Serve a single file:

`miniserve {{path/to/source_file}}`

- Require username/password:

`miniserve --auth {{username}}:{{password}} {{path/to/directory}}`
