# git push

> Invia i commit a un repository remoto.
> Maggiori informazioni: <https://git-scm.com/docs/git-push>.

- Invia le modifiche fatte nel ramo corrente locale al corrispondente ramo remoto:

`git push`

- Invia le modifiche fatte in uno specifico ramo locale al corrispondente ramo remoto:

`git push {{nome_repository_remoto}} {{nome_ramo}}`

- Pubblica il ramo corrente in un repository remoto, specificando il nome del ramo remoto:

`git push {{nome_repository_remoto}} -u {{nome_ramo_remoto}}`

- Invia le modifiche fatte in ogni ramo locale ai corrispondenti rami remoti:

`git push --all {{nome_repository_remoto}}`

- Cancella un ramo di un repository remoto:

`git push {{nome_repository_remoto}} --delete {{nome_ramo_remoto}}`

- Cancella i rami remoti che non hanno un ramo locale corrispondente:

`git push --prune {{nome_repository_remoto}}`

- Pubblica i tag che non sono già presenti nel repository remoto:

`git push --tags`
