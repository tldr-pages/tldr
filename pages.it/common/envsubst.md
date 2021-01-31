# envsubst

> Sostituisci variabili di ambiente con il loro valore in stringhe di formato della shell.
> Le variabili da sostituire devono essere nella forma `${var}` oppure `$var`.

- Sostituisci variabili di ambiente in stdin e stampa l'output su stdout:

`echo '{{$HOME}}' | envsubst`

- Sostituisci variabili di ambiente in un file input e stampa l'output su stdout:

`envsubst < {{percorso/a/file_input}}`

- Sostituisci variabili di ambiente in un file input e scrivi l'output su un file:

`envsubst < {{percorso/a/file_input}} > {{percorso/a/file_output}}`

- Sostituisci in un file input le variabili di ambiente specificate in una lista separata da spazi:

`envsubst {{$USER $HOME $SHELL}} < {{percorso/a/file_input}}`
