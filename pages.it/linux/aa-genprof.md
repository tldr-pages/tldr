# aa-genprof

> Genera profili di sicurezza AppArmor monitorando il comportamento dei programmi.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-genprof.8>.

- Avvia la generazione di un profilo per un programma:

`sudo aa-genprof {{percorso/del/programma}}`

- Specifica una directory personalizzata per i profili:

`sudo aa-genprof {{[-d|--dir]}} /{{path/to/profiles}} {{percorso/del/programma}}`

- Specifica un file di log personalizzato per la profilazione:

`sudo aa-genprof {{[-f|--file]}} /{{path/to/logfile}} {{percorso/del/programma}}`

- Mostra aiuto:

`aa-genprof {{[-h|--help]}}`
