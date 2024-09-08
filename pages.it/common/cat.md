# cat

> Stampa e concatena file.
> Maggiori informazioni: <https://manned.org/cat.1posix>.

- Stampa i contenuti di un file su standard output:

`cat {{file}}`

- Concatena più file in un unico file:

`cat {{file1}} {{file2}} > {{file_finale}}`

- Aggiungi il contenuto di diversi file alla fine di un file:

`cat {{file1}} {{file2}} >> {{file_finale}}`

- Numera tutte le linee stampate:

`cat -n {{file}}`
