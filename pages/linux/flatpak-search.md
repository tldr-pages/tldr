# flatpak search

> Search for applications and runtimes in all configured remotes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-search>.

- Search for a term in all configured remotes:

`flatpak search {{search-term}}`

- Search for a term among system-only installations:

`flatpak search --system {{search-term}}`

- Search for a term among user-only installations:

`flatpak search --user {{search-term}}`

- Display only specific columns (e.g. `Name`, `Description`, `Application`, `Remote`):

`flatpak search --columns={{Name,Application,Remote}} {{search-term}}`
