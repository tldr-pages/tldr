# convmv

> Conversione dei nomi dei file (NON del contenuto) da un encoding ad un altro.
> Maggiori informazioni: <https://www.j3e.de/linux/convmv/man/>.

- Controlla la conversione di encoding (non rinomina realmente il file):

`convmv -f {{encoding_originale}} -t {{encoding_finale}} {{file_input}}`

- Converti l'encoding del nome di un file e rinominalo utilizzando il nuovo encoding:

`convmv -f {{encoding_originale}} -t {{encoding_finale}} --notest {{file_input}}`
