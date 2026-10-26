# distrobox stop

> Stop a Distrobox container.
> Containers keep running after you leave them, so the next `distrobox enter` is faster.
> See also: `distrobox`.
> More information: <https://distrobox.it/usage/distrobox-stop/>.

- Stop a container:

`distrobox stop {{container_name}}`

- Stop a container without asking:

`distrobox stop {{[-Y|--yes]}} {{container_name}}`

- Stop every container:

`distrobox stop {{[-a|--all]}}`
