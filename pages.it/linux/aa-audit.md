# aa-audit

> Imposta i profili di sicurezza AppArmor in modalità audit.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- Imposta un profilo in modalità audit:

`sudo aa-audit {{nome_profilo}}`

- Imposta più profili in modalità audit:

`sudo aa-audit {{profilo1 profilo2 ...}}`

- Imposta un profilo in modalità audit da una directory specifica:

`sudo aa-audit {{[-d|--dir]}} /{{path/to/profiles}} {{nome_profilo}}`

- Forza la modalità audit anche se già applicata:

`sudo aa-audit --force {{nome_profilo}}`

- Imposta un profilo in modalità audit senza ricaricarlo:

`sudo aa-audit --no-reload {{nome_profilo}}`

- Rimuove la modalità audit per un profilo:

`sudo aa-audit {{[-r|--remove]}} {{nome_profilo}}`

- Mostra aiuto:

`aa-audit {{[-h|--help]}}`
