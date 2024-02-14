# pacman

> Gestore pacchetti di Arch Linux.
> Vedi anche: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Per comandi equivalenti in altri gestori pacchetti, vedi <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Maggiori informazioni: <https://man.archlinux.org/man/pacman.8>.

- Sincronizza e aggiorna tutti i pacchetti:

`sudo pacman -Syu`

- Installa un nuovo pacchetto:

`sudo pacman -S {{nome_pacchetto}}`

- Rimuovi un pacchetto e le sue dipendenze:

`sudo pacman -Rs {{nome_pacchetto}}`

- Cerca nel database un pacchetto contenente uno specifico file:

`pacman -F "{{nome_file}}"`

- Mostra i pacchetti installati e le versioni:

`pacman -Q`

- Mostra solo i pacchetti esplicitamente installati e le versioni:

`pacman -Qe`

- Mostra i pacchetti orfani (installati come dipendenze ma attualmente non richiesti da nessun altro pacchetto):

`pacman -Qtdq`

- Svuota l'intera cache di `pacman`:

`sudo pacman -Scc`
