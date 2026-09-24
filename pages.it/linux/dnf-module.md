# dnf module

> Gestisce la modularità dei pacchetti.
> Maggiori informazioni: <https://dnf.readthedocs.io/en/latest/command_ref.html#module-command>.

- Visualizza la panoramica della modularità:

`dnf module list`

- Visualizza la modularità di un programma specifico:

`dnf module list {{package_name}}`

- Imposta un pacchetto come abilitato:

`sudo dnf module enable {{package_name}}:{{stream}}`

- Abilita e installa una versione specifica:

`dnf module install {{package_name}}:{{stream}}`
