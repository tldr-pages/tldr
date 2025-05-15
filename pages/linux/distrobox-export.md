# distrobox-export

> Export app/service/binary from container to host OS. See also: `tldr distrobox`.
> More information: <https://distrobox.it/usage/distrobox-export>.

- Export an app from the container to the host (the desktop entry/icon will show up in your host system's application list):

`distrobox-export {{[-a|--app]}} {{package}} {{[-ef|--extra-flags]}} "--foreground"`

- Export a binary from the container to the host:

`distrobox-export {{[-b|--bin]}} {{path/to/binary}} {{[-ep|--export-path]}} {{path/to/binary_on_host}}`

- Export a binary from the container to the host (i.e.`$HOME/.local/bin`):

`distrobox-export {{[-b|--bin]}} {{path/to/binary}} {{[-ep|--export-path]}} {{path/to/export}}`

- Export a service from the container to the host (`--sudo` will run the service as root inside the container):

`distrobox-export --service {{package}} {{[-ef|--extra-flags]}} "--allow-newer-config" {{[-S|--sudo]}}`

- Unexport/delete an exported application:

`distrobox-export {{[-a|--app]}} {{package}} {{[-d|--delete]}}`
