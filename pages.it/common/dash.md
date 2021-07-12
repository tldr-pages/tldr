# dash

> Debian Almquist Shell, una implementazione di `sh` moderna, che conforme a POSIX, (non compatibile con Bash).
> Maggiori informazioni: <https://manned.org/dash>.

- Avvia una sessione shell interattiva:

`dash`

- Esegui un comando, ed esci subito:

`dash -c "{{command}}"`

- Esegui un script:

`dash {{percorsi/al/script.sh}}`

- Esegui comandi da un script, stampando ogni comando prima di eseguirlo:

`dash -x {{path/to/script.sh}}`

- Esegui comandi da un script, fermandosi al primo errore:

`dash -e {{path/to/script.sh}}`

- Leggi ed esegui commandi dal stdin:

`dash -s`
