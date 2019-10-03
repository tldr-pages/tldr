# git bisect

> Usa la ricerca binaria per trovare il commit che ha introdotto un bug.
> Maggiori informazioni: <https://git-scm.com/docs/git-bisect>.

- Avvia una sessione di bisect su un intervallo di commit limitato da un commit "cattivo", noto per contenere il bug, e un commit "buono", precedente al presentarsi del bug:

`git bisect start {{commit_cattivo}} {{commit_buono}}`

- Per ogni commit selezionato da `git bisect`, contrassegnalo con "bad" (cattivo) o "good" (buono) dopo averlo verificato:

`git bisect {{good|bad}}`

- Una volta che `git bisect` ha individuato il commit che ha introdotto il bug, termina la sessione di bisect e torna al ramo precedente:

`git bisect reset`

- Ignora un commit durante la sessione di bisect:

`git bisect skip`
