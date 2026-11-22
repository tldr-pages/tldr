# flatpak remotes

> List remote repositories configured for Flatpak.
> See also: `flatpak`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remotes>.

- List all configured remotes:

`flatpak remotes`

- List remotes with all their details:

`flatpak remotes {{[-d|--show-details]}}`

- List remotes including disabled ones:

`flatpak remotes --show-disabled`

- List remotes of the current user installation only:

`flatpak remotes {{[-u|--user]}}`

- Show only the name, URL, and priority of each remote:

`flatpak remotes --columns name,url,priority`

- List the available columns:

`flatpak remotes --columns help`
