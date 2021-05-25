# git remote

> Gestisci i collegamenti remoti ("remote") di un repository locale.
> Maggiori informazioni: <https://git-scm.com/docs/git-remote>.

- Mostra l'elenco dei collegamenti remoti, con il loro nome e URL:

`git remote -v`

- Mostra informazioni su un remote:

`git remote show {{nome_remote}}`

- Aggiungi un remote:

`git remote add {{nome_remote}} {{url_remote}}`

- Modifica l'URL di un remote (usa `--add` per preservare gli URL esistenti):

`git remote set-url {{nome_remoto}} {{nuovo_url}}`

- Elimina un remote:

`git remote remove {{nome_remote}}`

- Rinomina un remote:

`git remote rename {{vecchio_nome}} {{nuovo_nome}}`
