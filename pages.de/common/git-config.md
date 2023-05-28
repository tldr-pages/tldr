# git config

> Verwalten von benutzerdefinierten Optionen für Git Repositories.
> Diese Optionen können lokal (für das aktiven Repository) or global (für den aktiven Benutzer) sein.
> Weitere Informationen: <https://git-scm.com/docs/git-config/de>.

- Auflisten von lokalen Konfigurationseinträgen (gespeichert unter `.git/config` im aktiven Repository):

`git config --list --local`

- Auflisten von global Konfigurationseinträgen (gespeichert unter `~/.gitconfig`):

`git config --list --global`

- Auflisten von System-Konfigurationseinträgen (gespeichert unter `/etc/gitconfig`), und deren Speicherort:

`git config --list --system --show-origin`

- Ermitteln des Wertes für einen bestimmten Konfigurationseintrag:

`git config alias.unstage`

- Setzen des globalen Wertes für einen bestimmten Konfigurationseintrag:

`git config --global alias.unstage "reset HEAD --"`

- Zurücketzen des globalen Wertes für einen bestimmten Konfigurationseintrag auf seinen Standardwert:

`git config --global --unset alias.unstage`

- Bearbeiten der Git-Konfiguration für das aktive Repository mit dem Standard-Editor:

`git config --edit`

- Bearbeiten der globalen Git-Konfiguration mit dem Standard-Editor:

`git config --global --edit`
