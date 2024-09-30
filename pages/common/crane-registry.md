# crane registry

> Serve a registry implementation.
> This sub-command serves a registry implementation on an automatically chosen port (:0), $PORT or --address.
> The command blocks while the server accepts pushes and pulls.
> Contents are can be stored in memory (when the process exits, pushed data is lost.), and disk (--disk).
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

- Serve a registry implementation:

`crane registry serve`

- Address to listen on:

`crane registry serve --address {{address_name}}`

- Path to a directory where blobs will be stored:

`crane registry serve --disk {{path/to/store_dir}}`

- Display help:

`crane registry {{-h|--help}}`

- Display help:

`crane registry serve {{-h|--help}}`
