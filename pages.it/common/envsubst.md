# envsubst

> Sostituisci variabili di ambiente con il loro valore in stringhe di formato della shell.
> Le variabili da sostituire devono essere nella forma `${var}` oppure `$var`.
> Maggiori informazioni: <https://www.gnu.org/software/gettext/manual/html_node/envsubst-Invocation.html>.

- Sostituisci variabili di ambiente in stdin e stampa l'output su stdout:

`echo '{{$HOME}}' | envsubst`

- Sostituisci variabili di ambiente in un file input e stampa l'output su stdout:

`envsubst < {{percorso/del/file_input}}`

- Sostituisci variabili di ambiente in un file input e scrivi l'output su un file:

`envsubst < {{percorso/del/file_input}} > {{percorso/del/file_output}}`

- Sostituisci in un file input le variabili di ambiente specificate in una lista separata da spazi:

`envsubst {{$USER $HOME $SHELL}} < {{percorso/del/file_input}}`
