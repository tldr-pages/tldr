# aa-decode

> Decodifica i log di audit di AppArmor in un formato leggibile.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-decode.8>.

- Decodifica una stringa esadecimale:

`aa-decode {{stringa_esadecimale}}`

- Decodifica un file di log:

`sudo aa-decode {{file_di_log}}`

- Decodifica i log da `stdin` (es. file reindirizzato):

`sudo aa-decode - < {{file_di_log}}`

- Mostra aiuto:

`aa-decode {{[-h|--help]}}`
