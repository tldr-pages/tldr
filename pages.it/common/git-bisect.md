# git bisect

> Usa la ricerca binaria per trovare il commit che ha introdotto un bug.
> Git salta automaticamente avanti ed indietro nell'albero dei commit per restringere progressivamente il campo fino al commit colpevole.
> Maggiori informazioni: <https://git-scm.com/docs/git-bisect>.

- Avvia una ricerca su un intervallo di commit definito dal commit "cattivo" contenente il bug ed un altro commit "buono" privo del bug (solitamente più vecchio):

`git bisect start {{commit_cattivo}} {{commit_buono}}`

- Contrassegna ogni commit selezionato da `git bisect` come "bad" (cattivo) o "good" (buono) dopo averlo testato per verificare la presenza del bug:

`git bisect {{good|bad}}`

- Una volta che `git bisect` ha individuato il commit che ha introdotto il bug, termina la sessione di ricerca e torna al ramo precedente:

`git bisect reset`

- Ignora un commit durante la ricerca (ad esempio uno che fallisce i test per un motivo diverso dal bug ricercato):

`git bisect skip`
