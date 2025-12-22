# aws cognito-idp

> 配置 Amazon Cognito 用户池及其用户和组，并对其进行身份验证。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/>.

- 创建一个新的 Cognito 用户池：

`aws cognito-idp create-user-pool --pool-name {{名称}}`

- 列出所有用户池：

`aws cognito-idp list-user-pools --max-results {{10}}`

- 删除指定的用户池：

`aws cognito-idp delete-user-pool --user-pool-id {{用户池_id}}`

- 在指定的用户池中创建一个用户：

`aws cognito-idp admin-create-user --username {{用户名}} --user-pool-id {{用户池_id}}`

- 列出指定用户池中的用户：

`aws cognito-idp list-users --user-pool-id {{用户池_id}}`

- 从指定的用户池中删除一个用户：

`aws cognito-idp admin-delete-user --username {{用户名}} --user-pool-id {{用户池_id}}`
