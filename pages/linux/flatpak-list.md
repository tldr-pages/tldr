# flatpak list

> List installed flatpak applications and runtimes.
> See also: `flatpak`, `flatpak info`, `flatpak install`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-list>.

- List all installed applications and runtimes:

`flatpak list`

- List installed applications only:

`flatpak list --app`

- List installed runtimes only:

`flatpak list --runtime`

- List all runtimes, including locale and debug extensions:

`flatpak list {{[-a|--all]}}`

- List applications and runtimes installed for the current user:

`flatpak list {{[-u|--user]}}`

- Show details such as origin and size:

`flatpak list {{[-d|--show-details]}}`
