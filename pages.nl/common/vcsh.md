# vcsh

> Versiebeheersysteem voor de home-directory met behulp van Git-repositories.
> Zie ook: `chezmoi`, `stow`, `tuckr`, `homeshick`.
> Meer informatie: <https://manned.org/vcsh>.

- Initialiseer een (lege) repository:

`vcsh init {{repository_naam}}`

- Kloon een repository naar een aangepaste mapnaam:

`vcsh clone {{git_url}} {{repository_naam}}`

- Toon alle beheerde repositories:

`vcsh list`

- Voer een Git-commando uit op een beheerde repository:

`vcsh {{repository_naam}} {{git_commando}}`

- Push/pull alle beheerde repositories naar/van remotes:

`vcsh {{push|pull}}`

- Schrijf een aangepast `.gitignore`-bestand voor een beheerde repository:

`vcsh write-gitignore {{repository_naam}}`
