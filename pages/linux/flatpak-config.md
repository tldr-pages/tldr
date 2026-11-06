# flatpak config

> Manage configuration for Flatpak.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-config>.

- Display all Flatpak configuration settings:

`flatpak config --list`

- Display the value of a specific configuration setting:

`flatpak config --get {{key}}`

- Set a configuration setting:

`flatpak config --set {{key}} {{value}}`

- Remove a configuration setting:

`flatpak config --unset {{key}}`

- Display system-wide configuration settings instead of per-user:

`flatpak config --system --list`
