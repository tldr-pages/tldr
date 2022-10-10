# node

> Piattaforma JavaScript Server-side (Node.js).
> Maggiori informazioni: <https://nodejs.org>.

- Esegue un file JavaScript:

`node {{percorso/del/file}}`

- Avvia una REPL (shell interattiva):

`node`

- Esegue il codice JavaScript che viene specificato come argomento:

`node -e "{{codice}}"`

- Mostra come risultato le versioni delle dipendenze di node:

`node -p "process.versions"`

- Attiva il debugger mettendo in pausa l'esecuzione fino a quando il codice sorgente viene caricato:

`node --no-lazy --inspect-brk {{percorso/del/file}}`
