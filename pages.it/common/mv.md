# mv

> Sposta o rinomina file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/mv>.

- Sposta file:

`mv {{percorso/del/sorgente}} {{percorso/del/destinazione}}`

- Sposta file senza chiedere conferma prima di sovrascrivere file esistenti:

`mv -f {{percorso/del/sorgente}} {{percorso/del/destinazione}}`

- Sposta file interattivamente, chiedendo conferma prima di sovrascrivere file esistenti:

`mv -i {{percorso/del/sorgente}} {{percorso/del/destinazione}}`

- Sposta file senza sovrascrivere file esistenti:

`mv -n {{percorso/del/sorgente}} {{percorso/del/destinazione}}`

- Sposta file in modalità verbosa, mostrando a schermo ogni file che viene spostato:

`mv -v {{percorso/del/sorgente}} {{percorso/del/destinazione}}`
