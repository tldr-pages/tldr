# crane

> Container images managing tool.
> Some subcommands such as `pull`, `push`, `copy`, etc. have their own usage documentation.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Build or pull images if they don't exists:

`crane up/lift {{[-d|--detach]}}`

- Start stopped container:

`crane start {{target}}`

- Stop running containers:

`crane stop {{target}}`

- Execute command in target container:

`crane exec {{target}} {{<cmd>}}`

- Remove stopped container:

`crane rm {{[-f|--force]}} {{target}}`

- Push containers to the regsitry:

`crane push {{target}}`

- Show container logs:

`crane logs {{target}}`

- Show container statuses:

`crane status`
