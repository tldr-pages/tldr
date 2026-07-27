# aa-status

> Elenca i moduli AppArmor attualmente caricati.
> Vedi anche: `aa-complain`, `aa-disable`, `aa-enforce`.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Controlla lo stato:

`sudo aa-status`

- Mostra lo stato in formato JSON:

`sudo aa-status --json`

- Mostra lo stato in formato JSON con formattazione:

`sudo aa-status --pretty-json`

- Mostra il numero di policy caricate:

`sudo aa-status --profiled`

- Mostra il numero di policy in enforce caricate:

`sudo aa-status --enforced`

- Mostra il numero di policy non in enforce caricate:

`sudo aa-status --complaining`

- Mostra il numero di policy in enforce che terminano i processi:

`sudo aa-status --kill`
