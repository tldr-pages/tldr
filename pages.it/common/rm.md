# rm

> Rimuovi file o cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/rm>.

- Rimuovi file:

`rm {{percorso/a/file1 percorso/a/file2 ...}}`

- Rimuovi ricorsivamente una directory e tutti i suoi contenuti:

`rm -r {{percorso/alla/directory}}`

- Rimuovi ricorsivamente una directory, senza chiedere conferma o mostrare messaggi di errore:

`rm -rf {{percorso/alla/directory}}`

- Rimuovi file interattivamente, chiedendo conferma prima di rimuovere ogni file:

`rm -i {{file(s)}}`

- Rimuovi file in modalità verbosa, scrivendo un messaggio a schermo per ogni file rimosso:

`rm -v {{percorso/a/un/file}}`
