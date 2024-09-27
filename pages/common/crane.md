# crane

> Container images managing tool.
> Some subcommands such as `append`, `auth`, `copy`, etc. have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Execute a Crane command:

`crane [flags] {{subcommand}}`

- Allow pushing non-distributable (foreign) layers:

`crane {{--allow-nondistributable-artifacts}}`

- Display help:

`crane {{-h|--help}}`

- Allow image references to be fetched without TLS:

`crane {{--insecure}}`

- Specify the platform in the form os/arch{{/variant}}{{:osversion}} (e.g. linux/amd64). (default all):

`crane  {{--platform}} {{platform}}`

- Enable debug logs:

`crane {{-v|--verbose}}`
