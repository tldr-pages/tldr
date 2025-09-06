# git send-email

> Invia una raccolta di patch via email.
> Le patch possono essere specificate come file, directory, o liste di revisione.
> Maggiori informazioni: <https://git-scm.com/docs/git-send-email>.

- Invia l'ultimo commit nel ramo corrente:

`git send-email -1`

- Invia un commit specifico:

`git send-email -1 {{commit}}`

- Invia 10 commit nel ramo corrente:

`git send-email {{-10}}`

- Invia un'email con un messaggio introduttivo alla serie di patch:

`git send-email -{{numero_di_commit}} --compose`

- Revisiona e modifica il messaggio email per ogni patch da inviare:

`git send-email -{{numero_di_commit}} --annotate`
