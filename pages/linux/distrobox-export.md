# distrobox-export

> Export app/service/binary from container to host OS.
> Subcommand of `distrobox`. More about distrobox: `tldr distrobox`.
> More information: <https://github.com/89luca89/distrobox/blob/main/docs/usage/distrobox-export.md>.

- Export an app (eg: gedit) from the container to the host (will show up in your host system's application list):

`distrobox-export --app {{gedit}} --extra-flags "--foreground"`

- Export a binary from the container to the host:

`distrobox-export --bin {{path/to/binary}} --export-path {{path/to/binary_on_host}}`

- Export a binary (eg: ranger) from the container to the host:

`distrobox-export --bin {{/usr/bin/ranger}} --export-path {{$HOME/.local/bin}}`

- Export a service (eg: syncthing) from container to the host (`--sudo` will run the service as root inside the container):

`distrobox-export --service {{syncthing}} --extra-flags "--allow-newer-config" --sudo`

- Unexport/delete an exported app (eg: gedit):

`distrobox-export --app {{gedit}} --delete`
