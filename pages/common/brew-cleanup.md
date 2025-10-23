# brew cleanup

> Remove stale lock files and outdated downloads for all formulas and casks.
> More information: <https://docs.brew.sh/Manpage#cleanup-options-formulacask->.

- Remove stale lock files and outdated downloads for all formulas/casks:

`brew cleanup`

- Remove stale lock files and outdated downloads for a specific formula/cask:

`brew cleanup {{formula|cask}}`

- Show what would be removed, but do not actually remove anything:

`brew cleanup {{[-n|--dry-run]}}`

- Display help:

`brew cleanup {{[-h|--help]}}`
