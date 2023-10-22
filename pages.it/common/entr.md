# entr

> Esegui comandi arbitrari al cambiamento di file.
> Maggiori informazioni: <https://manned.org/entr>.

- Ricompila con `make` se qualsiasi file in quasiasi sottodirectory cambia:

`{{ag -l}} | entr {{make}}`

- Ricompila e testa con `make` se qualsiasi file sorgente `.c` nella directory corrente cambia:

`{{ls *.c}} | entr {{'make && make test'}}`

- Invia il segnale `SIGTERM` ad un sottoprocesso ruby precedentemente avviato prima di eseguire `ruby main.rb`:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- Esegui un comando con il file cambiato (`/_`) come argomento:

`{{ls *.sql}} | entr {{psql -f}} /_`
