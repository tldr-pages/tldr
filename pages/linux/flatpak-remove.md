# flatpak remove

> Remove flatpak applications or runtimes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remove>.

- Remove an installed application:

`flatpak remove {{com.example.app}}`

- Remove an installed application along with its data:

`flatpak remove --delete-data {{com.example.app}}`

- Remove all unused applications:

`flatpak remove --unused`
