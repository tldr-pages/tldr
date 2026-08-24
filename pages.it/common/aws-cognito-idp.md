# aws cognito-idp

> Configura un pool di utenti Amazon Cognito, i suoi utenti e gruppi e li autentica.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/>.

- Crea un nuovo pool di utenti Cognito:

`aws cognito-idp create-user-pool --pool-name {{nome}}`

- Elenca tutti i pool di utenti:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Elimina un pool di utenti specifico:

`aws cognito-idp delete-user-pool --user-pool-id {{id_user_pool}}`

- Crea un utente in un pool specifico:

`aws cognito-idp admin-create-user --username {{nome_utente}} --user-pool-id {{id_user_pool}}`

- Elenca gli utenti di un pool specifico:

`aws cognito-idp list-users --user-pool-id {{id_user_pool}}`

- Elimina un utente da un pool specifico:

`aws cognito-idp admin-delete-user --username {{nome_utente}} --user-pool-id {{id_user_pool}}`
