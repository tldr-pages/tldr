# flatpak pin

> Pin runtimes so they are not removed automatically when they become unused.
> See also: `flatpak`, `flatpak uninstall`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-pin>.

- List pinned runtimes:

`flatpak pin`

- Pin runtimes matching a pattern:

`flatpak pin {{runtime/org.freedesktop.Platform/x86_64/24.08}}`

- Pin a runtime in the current user installation:

`flatpak pin {{[-u|--user]}} {{runtime/org.freedesktop.Platform/x86_64/24.08}}`

- Remove a pin:

`flatpak pin --remove {{runtime/org.freedesktop.Platform/x86_64/24.08}}`
