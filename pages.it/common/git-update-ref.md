# git update-ref

> Crea, aggiorna e cancella riferimenti Git.
> Maggiori informazioni: <https://git-scm.com/docs/git-update-ref>.

- Cancella un riferimento, utile per resettare il primo commit in modo soft:

`git update-ref -d {{HEAD}}`

- Aggiorna un riferimento con un messaggio:

`git update-ref -m {{messaggio}} {{HEAD}} {{4e95e05}}`
