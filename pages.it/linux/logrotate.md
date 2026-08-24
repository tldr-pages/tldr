# logrotate

> Ruota, comprime e invia via email i log di sistema.
> Maggiori informazioni: <https://manned.org/logrotate>.

- Attiva un'esecuzione manualmente:

`logrotate {{percorso/del/logrotate.conf}} --force`

- Esegui utilizzando un comando specifico per inviare rapporti via email:

`logrotate {{percorso/del/logrotate.conf}} --mail {{/usr/bin/mail_command}}`

- Esegui senza utilizzare un file di stato (blocco):

`logrotate {{percorso/del/logrotate.conf}} --state /dev/null`

- Esegui e salta il controllo del file di stato (blocco):

`logrotate {{percorso/del/logrotate.conf}} --skip-state-lock`

- Dì a `logrotate` di registrare l'output dettagliato nel file di log:

`logrotate {{percorso/del/logrotate.conf}} --log {{percorso/del/file_log}}`
