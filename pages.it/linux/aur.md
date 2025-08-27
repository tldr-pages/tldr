# aur

> Compila pacchetti dall’AUR e gestisci repository locali.
> Nota: è necessario definire un repository locale in `/etc/pacman.conf` e installare `vifm` per avere tutte le funzionalità.
> Maggiori informazioni: <https://github.com/aurutils/aurutils>.

- Inizializza il repository che corrisponde al percorso in `/etc/pacman.conf`:

`repo-add {{percorso/del/database.db.tar.gz}}`

- Cerca un pacchetto nel database AUR:

`aur search {{parola_chiave}}`

- Scarica uno o più pacchetti e le loro dipendenze dall’AUR, compilali e aggiungili a un repository locale:

`aur sync {{pacchetto1 pacchetto2 ...}}`

- Elenca i pacchetti disponibili nel tuo repository locale:

`aur repo {{[-l|--list]}}`

- Aggiorna i pacchetti del repository locale:

`aur sync {{[-u|--upgrades]}}`

- Pulisci i file di compilazione dopo l’installazione:

`aur sync {{[-C|--clean]}} {{pacchetto}}`

- Installa un pacchetto senza mostrare le modifiche in Vim e senza confermare l’installazione delle dipendenze:

`aur sync --noview {{[-n|--noconfirm]}} {{pacchetto}}`

- Rimuovi un pacchetto dai metadati del repository (non rimuove il file del pacchetto stesso):

`repo-remove {{percorso/del/database.db.tar.gz}} {{pacchetto}}`
