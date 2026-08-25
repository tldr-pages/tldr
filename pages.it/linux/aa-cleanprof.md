# aa-cleanprof

> Pulisce i profili di sicurezza AppArmor rimuovendo le regole inutilizzate.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- Pulisce un profilo per rimuovere le regole inutilizzate:

`sudo aa-cleanprof {{nome_profilo}}`

- Pulisce più profili contemporaneamente:

`sudo aa-cleanprof {{profilo1 profilo2 ...}}`

- Specifica la directory contenente i profili:

`sudo aa-cleanprof {{[-d|--dir]}} /{{path/to/profiles}} {{nome_profilo}}`

- Esegue silenziosamente senza richieste:

`sudo aa-cleanprof {{[-s|--silent]}} {{nome_profilo}}`

- Impedisce il ricaricamento del profilo dopo la pulizia:

`sudo aa-cleanprof --no-reload {{nome_profilo}}`

- Mostra aiuto:

`aa-cleanprof {{[-h|--help]}}`
