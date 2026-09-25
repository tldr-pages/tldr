# aa-remove-unknown

> Rimuove i profili AppArmor che non sono più presenti nella directory di configurazione.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-remove-unknown.8>.

- Esegue una simulazione per vedere quali profili verrebbero rimossi:

`sudo aa-remove-unknown -n`

- Rimuove effettivamente i profili:

`sudo aa-remove-unknown`

- Mostra aiuto:

`aa-remove-unknown {{[-h|--help]}}`
