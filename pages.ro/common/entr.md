# entr

> Executați comenzi arbitrare atunci când fișierele se modifică.
> Mai multe informaţii: <https://manned.org/entr>

- Reconstruiți cu `make` dacă orice fișier din orice subdirector se modifică:

`{{ag -l}} | entr {{make}}`

- Reconstruiți și testați cu `make `dacă există fișiere sursă `.c` din directorul curent se modifică:

`{{ls *.c}} | entr {{'make && make test'}}`

- Trimiteți un `SIGTERM `la orice subprocese rubinice depusă anterior înainte de a executa `ruby main.rb`:

`{{ls *.rb}} | entr -r {{ruby main.rb}}`

- Rulați o comandă cu fișierul modificat (`/_`) ca argument:

`{{ls *.sql}} | entr {{psql -f}} /_`
