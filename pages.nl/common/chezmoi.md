# chezmoi

> Beheer dotfiles op meerdere, diverse machines.
> Zie ook: `stow`, `tuckr`, `vcsh`, `homeshick`.
> Meer informatie: <https://www.chezmoi.io/reference/>.

- Stel `chezmoi` in en maak een Git-repository aan in `~/.local/share/chezmoi`:

`chezmoi init`

- Stel `chezmoi` in gebaseerd op een bestaande Git-repository:

`chezmoi init {{repository_url}}`

- Houd één of meer dotfiles bij:

`chezmoi add {{pad/naar/dotfile1 pad/naar/dotfile2 ...}}`

- Update repository met lokale wijzigingen:

`chezmoi re-add {{pad/naar/dotfile1 pad/naar/dotfile2 ...}}`

- Bewerk de source status van een bijgehouden bestand:

`chezmoi edit {{pad/naar/dotfile_of_symlink}}`

- Zie openstaande wijzigingen:

`chezmoi diff`

- Pas de wijzigingen toe:

`chezmoi apply`

- Haal wijzigingen op van een externe repository en pas deze toe:

`chezmoi update`
