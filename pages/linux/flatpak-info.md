# flatpak info

> Show information about an installed Flatpak application or runtime.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-info>.

- Show information about an installed application or runtime:

`flatpak info {{com.example.app}}`

- Show information about a specific branch:

`flatpak info {{com.example.app}} {{branch}}`

- Show the permissions:

`flatpak info {{[-M|--show-permissions]}} {{com.example.app}}`

- Show the on-disk location:

`flatpak info {{[-l|--show-location]}} {{com.example.app}}`

- Show the installed size:

`flatpak info {{[-s|--show-size]}} {{com.example.app}}`
