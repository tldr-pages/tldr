# gcrane

> Container images managing tool.
> This tool implements a superset of the `crane` commands, with additional commands that are specific to `gcr.io`.
> Some subcommands such as `append`, `auth`, `copy`, etc. have their own usage documentation found under `crane`.
> See also: `crane`.
> Some subcommands such as `completion`, `gc`, `help` are specific to gcrane and have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Execute a `gcrane` subcommand:

`gcrane [flags] {{subcommand}}`

- Allow pushing non-distributable (foreign) layers:

`gcrane --allow-nondistributable-artifacts`

- Allow image references to be fetched without TLS:

`gcrane --insecure`

- Specify the platform in the form os/arch{{/variant}}{{:osversion}} (e.g. linux/amd64). (default all):

`gcrane --platform {{platform}}`

- Enable debug logs:

`gcrane --verbose`

- Display help:

`gcrane --help`
