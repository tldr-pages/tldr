# aws cognito-idp

> Manage Amazon Cognito user pool and it's users and groups using the CLI.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- Create a cognito user pool:

`aws cognito-idp create-user-pool --pool-name {{name}}`

- List all user pools:

`aws cognito-idp list-user-pools --max-results 10`

- Delete a specific user pool:

`aws cognito-idp delete-user-pool --user-pool-id {{user-pool-id}}`

- Create a user in specific pool:

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{user-pool-id}}`

- List the users of a pool:

`aws cognito-idp list-users --user-pool-id {{user-pool-id}}`

- Delete a user in specific pool:

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{user-pool-id}}`
