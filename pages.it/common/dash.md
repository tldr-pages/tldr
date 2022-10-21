# dash

> Debian Almquist Shell, una implementazione di `sh` moderna, che conforme a POSIX, (non compatibile con Bash).
> Maggiori informazioni: <https://manned.org/dash>.

- Avvia una sessione shell interattiva:

`dash`

- Esegui un comando, ed esci subito:

`dash -c "{{comando}}"`

- Esegui un script:

`dash {{percorso/dello/script.sh}}`

- Esegui comandi da un script, stampando ogni comando prima di eseguirlo:

`dash -x {{percorso/dello/script.sh}}`

- Esegui comandi da un script, fermandosi al primo errore:

`dash -e {{percorso/dello/script.sh}}`

- Leggi ed esegui commandi dal stdin:

`dash -s`
