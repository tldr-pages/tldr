# git push

> Invia i commit ad un repository remoto.
> Maggiori informazioni: <https://git-scm.com/docs/git-push>.

- Invia le modifiche fatte nel ramo corrente locale al corrispondente ramo remoto:

`git push`

- Invia le modifiche fatte in uno specifico ramo locale al corrispondente ramo remoto:

`git push {{nome_repository_remoto}} {{nome_ramo}}`

- Invia le modifiche fatte in uno specifico ramo locale al corrispondente ramo remoto ed imposta il ramo remoto come destinazione di default per i push/pull del ramo locale:

`git push -u {{nome_repository_remoto}} {{nome_ramo}}`

- Invia le modifiche fatte in uno specifico ramo locale ad uno specifico ramo remoto:

`git push {{nome_repository_remoto}} {{nome_ramo}}:{{nome_ramo_remoto}}`

- Invia le modifiche fatte in ogni ramo locale ai corrispondenti rami remoti in uno specifico repository remoto:

`git push --all {{nome_repository_remoto}}`

- Cancella un ramo di un repository remoto:

`git push {{nome_repository_remoto}} --delete {{nome_ramo_remoto}}`

- Cancella i rami remoti che non hanno un ramo locale corrispondente:

`git push --prune {{nome_repository_remoto}}`

- Pubblica i tag che non sono già presenti nel repository remoto:

`git push --tags`
