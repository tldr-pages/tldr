# aws cognito-idp

> 配置 Amazon Cognito 用户池及其用户和组，并进行身份验证。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>。

- 创建新的 Cognito 用户池：

`aws cognito-idp create-user-pool --pool-name {{name}}`

- 列出所有用户池：

`aws cognito-idp list-user-pools --max-results {{10}}`

- 删除特定的用户池：

`aws cognito-idp delete-user-pool --user-pool-id {{user_pool_id}}`

- 在特定的用户池中创建用户：

`aws cognito-idp admin-create-user --username {{username}} --user-pool-id {{user_pool_id}}`

- 列出特定用户池中的用户：

`aws cognito-idp list-users --user-pool-id {{user_pool_id}}`

- 从特定用户池中删除用户：

`aws cognito-idp admin-delete-user --username {{username}} --user-pool-id {{user_pool_id}}`
