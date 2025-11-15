# git tag

> Crea, elenca, cancella o verifica tag.
> Un tag è un riferimento statico a uno specifico commit.
> Maggiori informazioni: <https://git-scm.com/docs/git-tag>.

- Mostra tutti i tag:

`git tag`

- Crea un tag con un nome, puntandolo al commit corrente:

`git tag {{nome_tag}}`

- Crea un tag con un nome, puntandolo ad un dato commit:

`git tag {{nome_tag}} {{commit}}`

- Crea un tag annotandolo con un messaggio:

`git tag {{nome_tag}} {{[-m|--message]}} {{messaggio_tag}}`

- Cancella un tag, dato il suo nome:

`git tag {{[-d|--delete]}} {{nome_tag}}`

- Scarica tag aggiornati da upstream:

`git fetch {{[-t|--tags]}}`

- Mostra tutti i tag i cui predecessori includono uno specifico commit:

`git tag --contains {{commit}}`
