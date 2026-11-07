# flatpak history

> Show historical changes to Flatpak installations on the system.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-history>.

- Display all Flatpak history entries:

`flatpak history`

- Display history entries for the current user instead of system-wide:

`flatpak history --user`

- Display history entries that occurred since a specific date or time:

`flatpak history --since {{time}}`

- Display history entries that occurred until a specific date or time:

`flatpak history --until {{time}}`

- Display history entries with the newest changes first:

`flatpak history --reverse`
