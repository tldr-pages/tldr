# flatpak pin

> Pin runtimes so they are not removed automatically when they become unused.
> See also: `flatpak`, `flatpak uninstall`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-pin>.

- List pinned patterns:

`flatpak pin`

- Pin runtimes matching a pattern:

`flatpak pin {{org.freedesktop.Platform//24.08}}`

- Pin a runtime in the current user installation:

`flatpak pin {{[-u|--user]}} {{org.freedesktop.Platform//24.08}}`

- Remove a pin (the pattern must match exactly as shown by `flatpak pin`):

`flatpak pin --remove {{org.freedesktop.Platform//24.08}}`
