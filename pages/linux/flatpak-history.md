# flatpak history

> Show the history of changes to installed applications and runtimes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-history>.

- Show the history of changes (system-wide installations):

`flatpak history`

- Show the history of changes for user-only installations:

`flatpak history --user`

- Include runtimes that are not used by any installed application:

`flatpak history --show-unused`

- Show the history of changes for a specific application:

`flatpak history {{com.example.app}}`

- Display only specific columns (e.g. `Change`, `ChangeTime`, `Application`, `Remote`):

`flatpak history --columns={{Change,ChangeTime,Application}}`
