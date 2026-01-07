# difft

> Confronta file o directory in base alla sintassi del linguaggio di programmazione.
> Vedi anche: `delta`, `diff`.
> Maggiori informazioni: <https://difftastic.wilfred.me.uk/introduction.html>.

- Confronta due file o directory:

`difft {{percorso/del/file_o_directory1}} {{percorso/del/file_o_directory2}}`

- Segnala solo la presenza di differenze tra i file:

`difft --check-only {{percorso/del/file1}} {{percorso/del/file2}}`

- Specifica la modalità di visualizzazione (default è `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{percorso/del/file1}} {{percorso/del/file2}}`

- Ignora i commenti durante il confronto:

`difft --ignore-comments {{percorso/del/file1}} {{percorso/del/file2}}`

- Abilita/Disabilita la colorazione sintattica del codice sorgente (default è `on`):

`difft --syntax-highlight {{on|off}} {{percorso/del/file1}} {{percorso/del/file2}}`

- Non outputta nulla se non ci sono differenze tra i file:

`difft --skip-unchanged {{percorso/del/file_o_directory1}} {{percorso/del/file_o_directory2}}`

- Stampa tutti i linguaggi di programmazione supportati dallo strumento, con le loro estensioni:

`difft --list-languages`
