# aws cognito-idp

> Verwalten des Amazon Cognito-Benutzerpools, seiner Benutzer und Gruppen mit der CLI.
> Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>

- Erstelle einen neuen Cognito-Benutzerpool:

`aws cognito-idp create-user-pool --pool-name {{name}}`

- Liste alle Bentzerpools auf:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Lösche einen bestimmten Benutzerpool:

`aws cognito-idp delete-user-pool --user-pool-id {{user_pool_id}}`

- Erstelle einen Benutzer in einem bestimmten Pool:

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{user_pool_id}}`

- Die Benutzer eines bestimmten Pool auflisten:

`aws cognito-idp list-users --user-pool-id {{user_pool_id}}`

- Einen bestimmten Benutzer aus einem Pool löschen:

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{user_pool_id}}`
