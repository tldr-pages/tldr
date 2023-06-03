# aws cognito-idp

> Verwalten des Amazon Cognito-Benutzerpool, seine Benutzer und Gruppen mit der CLI.
> Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>

- Einen neuen Cognito user pool erstellen:

`aws cognito-idp create-user-pool --pool-name {{name}}`

- Alle Bentzerpools auflisten:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Einen bestimmten Benutzerpool löschen:

`aws cognito-idp delete-user-pool --user-pool-id {{user_pool_id}}`

- Einen bestimmten Benutzer im Pool erstellen:

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{user_pool_id}}`

- Die Benutzer eines bestimmten Pool auflisten:

`aws cognito-idp list-users --user-pool-id {{user_pool_id}}`

- Einen bestimmten Benutzer aus einem Pool löschen:

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{user_pool_id}}`
