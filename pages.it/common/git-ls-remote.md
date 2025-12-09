# git ls-remote

> Elenca i riferimenti in un repository remoto dato un nome o un URL.
> Qualora né nome né URL siano specificati, il ramo predefinito è upstream - se configurato - oppure origin.
> Maggiori informazioni: <https://git-scm.com/docs/git-ls-remote>.

- Mostra tutti i riferimenti nel repository remoto predefinito:

`git ls-remote`

- Mostra solo i riferimenti HEAD nel repository remoto predefinito:

`git ls-remote --heads`

- Mostra solo i riferimenti a tag nel repository remoto predefinito:

`git ls-remote --tags`

- Mostra tutti i riferimenti da un repository remoto dato un nome o URL:

`git ls-remote {{url_repository}}`

- Filtra i riferimenti da un repository remoto rispetto a un dato criterio:

`git ls-remote {{nome_repository}} "{{criterio}}"`
