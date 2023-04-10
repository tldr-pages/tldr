# log

> Visualizza, esporta e configura i sistemi di log.
> Maggiori informazioni: <https://www.dssw.co.uk/reference/log.html>.

- Mostra i log di sistema in diretta:

`log stream`

- Mostra i log mandati a `syslog` da processi con un PID specifico:

`log stream --process {{ID_processo}}`

- Mostra i log mandati a `syslog` da processi con un nome specifico:

`log show --predicate "process == '{{process_name}}'"`

- Esporta sul disco tutti i log dell'ultima ora:

`sudo log collect --last {{1h}} --output {{percorso/del/file.logarchive}}`
