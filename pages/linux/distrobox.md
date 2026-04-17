# distrobox

> Use any Linux distribution inside your terminal in a container.
> Integrates tightly with the host, sharing the home directory, hardware, and graphical apps.
> Some subcommands such as `create`, `enter`, and `export` have their own usage documentation.
> More information: <https://distrobox.it>.

- List all containers:

`distrobox list`

- Create a new container from an image:

`distrobox create --name {{container_name}} --image {{ubuntu:22.04}}`

- Enter a container:

`distrobox enter {{container_name}}`

- Upgrade all containers:

`distrobox upgrade --all`

- Stop a running container:

`distrobox stop {{container_name}}`

- Remove a container:

`distrobox rm {{container_name}}`
