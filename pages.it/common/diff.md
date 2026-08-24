# diff

> Confronta file e directory.
> Vedi anche: `delta`, `difft`.
> Maggiori informazioni: <https://manned.org/diff>.

- Confronta file (elenca i cambiamenti per trasformare `file_vecchio` in `file_nuovo`):

`diff {{file_vecchio}} {{file_nuovo}}`

- Confronta file, ignorando gli spazi bianchi:

`diff {{[-w|--ignore-all-space]}} {{file_vecchio}} {{file_nuovo}}`

- Confronta file, mostrando le differenze affiancate:

`diff {{[-y|--side-by-side]}} {{file_vecchio}} {{file_nuovo}}`

- Confronta file, mostrando le differenze in formato unificato (come usato da `git diff`):

`diff {{[-u|--unified]}} {{file_vecchio}} {{file_nuovo}}`

- Confronta directory ricorsivamente (mostra i nomi dei file/directory diversi e le modifiche ai file):

`diff {{[-r|--recursive]}} {{old_directory}} {{new_directory}}`

- Confronta directory, mostrando solo i nomi dei file diversi:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{old_directory}} {{new_directory}}`

- Crea un file patch per Git dalle differenze di due file di testo, trattando i file inesistenti come vuoti:

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{file_vecchio}} {{file_nuovo}} > {{diff.patch}}`

- Confronta file, mostrando l'output colorato e cercando duramente un insieme minimo di cambiamenti:

`diff {{[-d|--minimal]}} --color=always {{file_vecchio}} {{file_nuovo}}`
