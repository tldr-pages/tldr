# flatpak kill

> Stop a running Flatpak application.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-kill>.

- Stop a running application by its application ID:

`flatpak kill {{com.example.app}}`

- Stop a specific running instance by its instance ID (use `flatpak ps` to find the instance ID):

`flatpak kill {{instance_id}}`
