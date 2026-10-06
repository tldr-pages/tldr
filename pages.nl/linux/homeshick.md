# homeshick

> Synchroniseer Git-dotfiles.
> Zie ook: `chezmoi`, `stow`, `tuckr`, `vcsh`.
> Meer informatie: <https://github.com/andsens/homeshick/wiki>.

- Maak een nieuw castle aan:

`homeshick generate {{castle_naam}}`

- Voeg een bestand toe aan je castle:

`homeshick track {{castle_naam}} {{pad/naar/bestand}}`

- Ga naar een castle:

`homeshick cd {{castle_naam}}`

- Kloon een castle:

`homeshick clone {{github_gebruikersnaam}}/{{repository_naam}}`

- Symlink alle bestanden van een castle:

`homeshick link {{castle_naam}}`
