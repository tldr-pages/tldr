# rm

> Rimuovi file o cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/rm>.

- Rimuovi file:

`rm {{percorso/del/file1 percorso/del/file2 ...}}`

- Rimuovi ricorsivamente una cartella e tutti i suoi contenuti:

`rm -r {{percorso/della/cartella}}`

- Rimuovi ricorsivamente una cartella, senza chiedere conferma o mostrare messaggi di errore:

`rm -rf {{percorso/della/cartella}}`

- Rimuovi file interattivamente, chiedendo conferma prima di rimuovere ogni file:

`rm -i {{file(s)}}`

- Rimuovi file in modalità verbosa, scrivendo un messaggio a schermo per ogni file rimosso:

`rm -v {{percorso/del/file}}`
