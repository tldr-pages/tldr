# git diff

> Mostra le modifiche ai file tracciati.
> Maggiori informazioni: <https://git-scm.com/docs/git-diff>.

- Mostra le modifiche non ancora nell'area di stage:

`git diff`

- Mostra tutte le modifiche non ancora salvate in un commit (incluse quelle nell'area di stage):

`git diff HEAD`

- Mostra solo le modifiche nell'area di stage (aggiunte, ma non ancora committate):

`git diff --staged`

- Mostra le modifiche di tutti i commit a partire da una certa data/ora (un'espressione temporale come "1 week 2 days" o una data ISO):

`git diff 'HEAD@{3 months|weeks|days|hours|seconds ago}'`

- Mostra solo i nomi dei file modificati a partire da un dato commit:

`git diff --name-only {{commit}}`

- Stampa un riepilogo dei file creati, rinominati o la cui modalità è cambiata a partire da un dato commit:

`git diff --summary {{commit}}`

- Confronta le versioni di un dato file tra due rami o commit:

`git diff {{ramo_1}}..{{ramo_2}} [--] {{percorso/del/file}}`

- Confronta le versioni di più file tra il ramo corrente e un altro ramo:

`git diff {{ramo}}:{{percorso/del/file2}} {{percorso/del/file}}`
