# flatpak remotes

> List remote repositories configured for Flatpak.
> See also: `flatpak`, `flatpak-remote-info`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remotes>.

- List configured remotes for both user and system installations:

`flatpak remotes`

- List remotes with all their details:

`flatpak remotes {{[-d|--show-details]}}`

- List remotes including disabled ones:

`flatpak remotes --show-disabled`

- List remotes of the current user installation only:

`flatpak remotes {{[-u|--user]}}`

- Show specific columns of information:

`flatpak remotes --columns {{name,url,priority,...}}`

- List the available columns:

`flatpak remotes --columns help`
