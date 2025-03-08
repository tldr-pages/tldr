# git archive

> Crea un archivio dei file nell'albero di lavoro.
> Maggiori informazioni: <https://git-scm.com/docs/git-archive>.

- Crea un archivio tar del contenuto in HEAD e stampa il risultato su standard output:

`git archive {{[-v|--verbose]}} HEAD`

- Crea un archivio zip del contenuto in HEAD e stampa il risultato su standard output:

`git archive {{[-v|--verbose]}} --format zip HEAD`

- Come sopra, ma scrivi l'archivio zip su file:

`git archive {{[-v|--verbose]}} {{[-o|--output]}} {{percorso/del/file.zip}} HEAD`

- Crea un archivio tar dell'ultimo commit sul ramo specificato:

`git archive {{[-o|--output]}} {{percorso/del/file.tar}} {{nome_ramo}}`

- Crea un archivio tar del contenuto di una specifica directory:

`git archive {{[-o|--output]}} {{percorso/del/file.tar}} HEAD:{{percorso/della/directory}}`

- Anteponi un percorso ad ogni file cosí da archiviarlo in una directory specifica:

`git archive {{[-o|--output]}} {{percorso/del/file.tar}} --prefix {{percorso/da/anteporre}}/ HEAD`
