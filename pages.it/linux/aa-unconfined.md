# aa-unconfined

> Elenca i processi con porte TCP/UDP aperte che non hanno profili AppArmor caricati.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-unconfined.8>.

- Elenca i processi non confinati usando il comando `ss` (predefinito):

`sudo aa-unconfined`

- Usa `netstat` invece di `ss` per rilevare i socket di rete aperti:

`sudo aa-unconfined --with-netstat`

- Mostra tutti i processi da `/proc` con porte TCP/UDP e nessun profilo AppArmor (più dettagliato):

`sudo aa-unconfined --paranoid`

- Mostra aiuto:

`aa-unconfined {{[-h|--help]}}`
