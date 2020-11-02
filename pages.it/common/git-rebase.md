# git rebase

> Applica i commit di un ramo su un ramo differente.
> Tipicamente usato per riallineare (rebase) due rami, creando copie dei commit nella nuova posizione.
> Maggiori informazioni: <https://git-scm.com/docs/git-rebase>.

- Riallinea il ramo corrente con il ramo specificato:

`git rebase {{ramo_della_nuova_base}}`

- Avvia un rebase interattivo, che consente di riordinare, omettere, unire o modificare i commit:

`git rebase -i {{nome_ramo_o_commit_hash}}`

- Prosegui con un rebase che era stato sospeso da un errore di unione, dopo aver risolto i conflitti:

`git rebase --continue`

- Prosegui con un rebase che era stato sospeso da conflitti di unione, ignorando i commit in conflitto:

`git rebase --skip`

- Interrompi un rebase in corso (ad esempio perché interrotto da un conflitto di unione):

`git rebase --abort`

- Sposta parti del ramo corrente su una base differente, specificando la vecchia base di partenza:

`git rebase --onto {{nuova_base}} {{vecchia_base}}`

- Applica gli ultimi 5 commit locali, consentendo di riordinarli, ometterli, unirli o modificarli:

`git rebase -i {{HEAD~5}}`

- Risolvi automaticamente i conflitti a favore del ramo di versione corrente (la parola chiave `theirs` ha qui un significato opposto):

`git rebase -X theirs {{nome_ramo}}`
