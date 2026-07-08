# container

> Create and run Linux containers as lightweight virtual machines on macOS.
> Some subcommands such as `build`, `exec`, `image`, `run`, and `system` have their own usage documentation.
> More information: <https://github.com/apple/container>.

- Start the container services:

`container system start`

- Build an image from the current directory and tag it:

`container build -t {{image:tag}} .`

- Run an interactive shell in a new container:

`container run {{[-it\|--interactive --tty]}} {{image:tag}} {{/bin/bash}}`

- List running containers:

`container ls`

- Execute a shell in a running container:

`container exec {{[-it\|--interactive --tty]}} {{container_name}} {{/bin/sh}}`

- Display help:

`container {{[-h|--help]}}`

- Display version:

`container --version`
