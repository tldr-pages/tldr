# toolbox

> Manage containerized command-line environments on Linux.
> Some subcommands such as `create` have their own usage documentation.
> More information: <https://manned.org/toolbox>.

- Enter a Toolbx container to use it interactively:

`toolbox enter {{container}}`

- Remove one or more containers:

`toolbox rm {{container1 container2 ...}}`

- Remove one or more images:

`toolbox rmi {{image1 image2 ...}}`

- Display help for a specific subcommand (such as `create`, `enter`, `rm`, etc.):

`toolbox help {{subcommand}}`

- Display help:

`toolbox {{[-h|--help]}}`

- Display version:

`toolbox --version`
