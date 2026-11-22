# flatpak permissions

> List permissions that applications have been granted in the permission store, such as for notifications or screenshots.
> See also: `flatpak`, `flatpak override`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-permissions>.

- List all permission entries:

`flatpak permissions`

- List permission entries in a specific table:

`flatpak permissions {{notifications}}`

- List permission entries for a specific ID in a table:

`flatpak permissions {{notifications}} {{notification}}`

- Show all permissions for a specific application:

`flatpak permission-show {{com.example.app}}`

- Reset all permissions for a specific application:

`flatpak permission-reset {{com.example.app}}`
