# clear

> Pulisce lo schermo del terminale.
> Maggiori informazioni: <https://manned.org/clear>.

- Pulisci lo schermo:

`clear`

- Pulisci lo schermo ma mantieni il buffer di scorrimento del terminale (equivalente a premere `<Ctrl l>` in Bash):

`clear -x`

- Indica il tipo di terminale da pulire (predefinito: il valore della variabile d'ambiente `$TERM`):

`clear -T {{tipo_di_terminale}}`

- Mostra la versione di `ncurses` usata da `clear`:

`clear -V`
