# crane

> Container images managing tool.
> Some subcommands such as `pull`, `push`, `copy`, etc. have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Execute a `crane` subcommand:

`crane {{subcommand}}`

- Allow pushing non-distributable (foreign) layers:

`crane --allow-nondistributable-artifacts {{subcommand}}`

- Allow image references to be fetched without TLS:

`crane --insecure {{subcommand}}`

- Specify the platform in the form os/arch{{/variant}}{{:osversion}} (e.g. linux/amd64). (default all):

`crane --platform {{platform}} {{subcommand}}`

- Enable debug logs for a subcommand:

`crane {{[-v|--verbose]}} {{subcommand}}`

- Display help for a subcommand:

`crane {{[-h|--help]}} {{subcommand}}`
