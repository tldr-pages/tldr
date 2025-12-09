# cat

> Stampa e concatena file.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- Stampa il contenuto di un file su `stdout`:

`cat {{percorso/del/file}}`

- Concatena diversi file in un file di output:

`cat {{percorso/del/file1 percorso/del/file2 ...}} > {{percorso/dell/output}}`

- Aggiunge diversi file a un file di output:

`cat {{percorso/del/file1 percorso/del/file2 ...}} >> {{percorso/dell/output}}`

- Scrive in un file in modo interattivo:

`cat > {{percorso/del/file}}`

- Numera tutte le righe di output:

`cat {{[-n|--number]}} {{percorso/del/file}}`

- Visualizza tutti i caratteri, inclusi tabulazioni, terminazioni di riga e caratteri non stampabili:

`cat {{[-A|--show-all]}} {{percorso/del/file}}`

- Passa il contenuto del file a un altro programma tramite `stdin`:

`cat {{percorso/del/file}} | {{programma}}`
