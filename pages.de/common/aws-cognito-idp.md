# aws cognito-idp

> Verwalten des Amazon Cognito-Benutzerpools, seiner Benutzer und Gruppen mit der CLI.
> Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/>.

- Erstelle einen neuen Cognito-Benutzerpool:

`aws cognito-idp create-user-pool --pool-name {{name}}`

- Liste alle Bentzerpools auf:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Lösche einen bestimmten Benutzerpool:

`aws cognito-idp delete-user-pool --user-pool-id {{benutzerpool_id}}`

- Erstelle einen Benutzer in einem bestimmten Pool:

`aws cognito-idp admin-create-user --username {{benutzer}} --user-pool-id {{benutzerpool_id}}`

- Liste die Benutzer eines bestimmten Pool auf:

`aws cognito-idp list-users --user-pool-id {{benutzerpool_id}}`

- Lösche einen Benutzer aus einem bestimmten Pool:

`aws cognito-idp admin-delete-user --username {{benutzer}} --user-pool-id {{benutzerpool_id}}`
