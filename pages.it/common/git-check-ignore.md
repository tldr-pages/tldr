# git check-ignore

> Analizza ed esegui il debug di ".gitignore" e dei file esclusi.
> Maggiori informazioni: <https://git-scm.com/docs/git-check-ignore>.

- Verifica se un file o una directory sono ignorati:

`git check-ignore {{percorso/del/file_o_directory}}`

- Verifica se più file o directory sono ignorati:

`git check-ignore {{percorso/del/file_o_directory1 percorso/del/file_o_directory2 ...}}`

- Leggi i percorsi di file o directory da `stdin` (uno per riga) invece che dalla riga di comando:

`git check-ignore --stdin < {{percorso/della/lista_dei_file_o_directory}}`

- Non controllare nell'indice (usato per determinare il motivo per cui alcuni percorsi non sono ignorati):

`git check-ignore --no-index {{percorso/del/file_o_directory1 percorso/del/file_o_directory2 ...}}`

- Includi dettagli sul pattern corrispondente per ogni percorso specificato:

`git check-ignore --verbose {{percorso/del/file_o_directory1 percorso/del/file_o_directory2 ...}}`
