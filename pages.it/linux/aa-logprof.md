# aa-logprof

> Aggiorna interattivamente i profili di sicurezza AppArmor basandosi sulle violazioni registrate.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-logprof.8>.

- Esamina e aggiorna interattivamente i profili basandosi sui log di sistema:

`sudo aa-logprof`

- Usa una directory specifica per i profili AppArmor:

`sudo aa-logprof {{[-d|--dir]}} /{{path/to/profiles}}`

- Usa un file di log specifico invece di quello predefinito:

`sudo aa-logprof {{[-f|--file]}} /{{path/to/logfile}}`

- Ignora tutte le voci di log precedenti al marcatore specificato:

`sudo aa-logprof {{[-m|--logmark]}} "{{testo_marcatore_log}}"`

- Mostra aiuto:

`aa-logprof {{[-h|--help]}}`
