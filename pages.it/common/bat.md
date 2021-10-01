# bat

> Stampa e concatena file.
> Un clone di `cat` con syntax highlighting e integrazione Git.
> Maggiori informazioni: <https://github.com/sharkdp/bat>.

- Stampa i contenuti di un file su standard output:

`bat {{file}}`

- Concatena diversi file in un unico file:

`bat {{file1}} {{file2}} > {{file_finale}}`

- Aggiungi il contenuto di diversi file alla fine di un file:

`bat {{file1}} {{file2}} >> {{file_finale}}`

- Numera tutte le linee stampate:

`bat -n {{file}}`

- Evidenzia la sintassi di un file JSON:

`bat --language json {{file.json}}`

- Mostra tutti i linguaggi supportati:

`bat --list-languages`
