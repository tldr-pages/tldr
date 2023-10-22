# git log

> Mostra la cronologia dei commit.
> Maggiori informazioni: <https://git-scm.com/docs/git-log>.

- Mostra la sequenza dei commit del ramo del repository in uso, a partire dal commit corrente e andando in ordine cronologico inverso:

`git log`

- Mostra la cronologia di un dato file o directory, mostrando anche le modifiche:

`git log -p {{percorso/del/file_o_directory}}`

- Offri una panoramica dei file che sono cambiati ad ogni commit:

`git log --stat`

- Mostra il grafo dei commit nel ramo corrente, includendo solo la prima riga di ogni messaggio di commit:

`git log --oneline --graph`

- Mostra il grafo di tutti i commit, tag e rami dell'intero repository:

`git log --oneline --decorate --all --graph`

- Mostra solo i commit il cui messaggio contiene una data stringa (ignorando maiuscole/minuscole):

`git log -i --grep {{stringa_da_cercare}}`

- Mostra gli ultimi N commit di un certo autore:

`git log -n {{numero}} --author={{autore}}`

- Mostra i commit effettuati tra due date (yyyy-mm-dd):

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
