# git check-ignore

> Analizza ed esegui il debug di ".gitignore" e dei file esclusi.
> Maggiori informazioni: <https://git-scm.com/docs/git-check-ignore>.

- Verifica se un file o una cartella sono ignorati:

`git check-ignore {{percorso/del/file_o_cartella}}`

- Verifica se più file o cartelle sono ignorati:

`git check-ignore {{percorso/del/file}} {{percorso/alla/cartella}}`

- Leggi i percorsi di file o cartelle da stdin (uno per riga) invece che dalla riga di comando:

`git check-ignore --stdin < {{percorso/alla/lista_dei_file_o_cartelle}}`

- Non controllare nell'indice (usato per determinare il motivo per cui alcuni percorsi non sono ignorati):

`git check-ignore --no-index {{percorsi/ai/file_o_cartelle}}`

- Includi dettagli sul pattern corrispondente per ogni percorso specificato:

`git check-ignore --verbose {{percorsi/ai/file_o_cartelle}}`
