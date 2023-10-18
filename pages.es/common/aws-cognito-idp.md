# aws cognito-idp

> Administra el grupo de usuarios de Amazon Cognito y sus usuarios y grupos utilizando la CLI.
> Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- Crea un nuevo grupo de usuarios de Cognito:

`aws cognito-idp create-user-pool --pool-name {{nombre}}`

- Lista todos los grupos de usuarios:

`aws cognito-idp list-user-pools --max-results {{10}}`

- Elimina un grupo de usuarios específico:

`aws cognito-idp delete-user-pool --user-pool-id {{user_pool_id}}`

- Crea un usuario en un grupo específico:

`aws cognito-idp admin-create-user --username {{nombre_usuario}} --user-pool-id {{user_pool_id}}`

- Lista los usuarios de un pool específico:

`aws cognito-idp list-users --user-pool-id {{user_pool_id}}`

- Elimina un usuario de un grupo específico:

`aws cognito-idp admin-delete-user --username {{nombre_usuario}} --user-pool-id {{user_pool_id}}`
