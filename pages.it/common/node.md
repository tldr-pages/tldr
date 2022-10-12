# node

> Piattaforma JavaScript Server-side (Node.js).
> Maggiori informazioni: <https://nodejs.org>.

- Esegue un file JavaScript:

`node {{percorso/al/file}}`

- Avvia una REPL (shell interattiva):

`node`

- Esegue il codice JavaScript che viene specificato come argomento:

`node -e "{{codice}}"`

- Valuta un'espressione e ne stampa il risultato, questo comando specifico è utile per vedere le versioni delle dipendenze di node:

`node -p "process.versions"`

- Attiva il debugger mettendo in pausa l'esecuzione finché il codice sorgente non viene caricato:

`node --no-lazy --inspect-brk {{percorso/al/file}}`
