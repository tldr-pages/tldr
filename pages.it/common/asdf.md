# asdf

> Interfaccia da linea di comando per gestire le versionai di diversi pacchetti.
> Maggiori informazioni: <https://asdf-vm.com/manage/commands.html>.

- Elenca tutti i plugin disponibili:

`asdf plugin list all`

- Installa un plugin:

`asdf plugin add {{nome}}`

- Elenca tutte le versioni disponibili per un pacchetto:

`asdf list all {{nome}}`

- Installa una specifica versione di un pacchetto:

`asdf install {{nome}} {{versiona}}`

- Imposta la versione globale per un pacchetto:

`asdf set -u {{nome}} {{versiona}}`

- Imposta la versiona locale per un pacchetto:

`asdf set {{nome}} {{versiona}}`

- Elenca la versione utilizzata per un pacchetto:

`asdf current {{nome}}`
