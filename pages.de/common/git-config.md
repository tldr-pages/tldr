# git config

> Verwalten von benutzerdefinierten Optionen für Git Repositories.
> Diese Optionen können lokal (für das aktiven Repository) or global (für den aktiven Benutzer) sein.
> Weitere Informationen: <https://git-scm.com/docs/git-config/de>.

- Liste nur lokale Konfigurationseinträge (gespeichert unter `.git/config` im aktiven Repository) auf:

`git config --list --local`

- Liste nur globale Konfigurationseinträge (gespeichert unter `~/.gitconfig`) auf:

`git config --list --global`

- Liste nur System-Konfigurationseinträge (gespeichert unter `/etc/gitconfig`) und deren Speicherort auf:

`git config --list --system --show-origin`

- Gib den Wert eines bestimmten Konfigurationseintrags aus:

`git config alias.unstage`

- Setze den globalen Wert eines bestimmten Konfigurationseintrags:

`git config --global alias.unstage "reset HEAD --"`

- Setze den globalen Wert eines bestimmten Konfigurationseintrags auf seinen Standardwert zurück:

`git config --global --unset alias.unstage`

- Bearbeite die Git-Konfiguration für das aktuelle Repository mit dem Standard-Editor:

`git config --edit`

- Bearbeite die globale Git-Konfiguration mit dem Standard-Editor:

`git config --global --edit`
