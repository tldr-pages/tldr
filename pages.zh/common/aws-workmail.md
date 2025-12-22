# aws workmail

> 管理 Amazon WorkMail。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/workmail/>.

- 列出所有 WorkMail 组织：

`aws workmail list-organizations`

- 列出指定组织中的所有用户：

`aws workmail list-users --organization-id {{组织 ID}}`

- 在指定组织中创建一个 WorkMail 用户：

`aws workmail create-user --name {{用户名}} --display-name {{显示名称}} --password {{密码}} --organization-id {{组织 ID}}`

- 将一个组或用户注册并启用到 WorkMail：

`aws workmail register-to-work-mail --entity-id {{实体 ID}} --email {{电子邮件}} --organization-id {{组织 ID}}`

- 在指定组织中创建一个 WorkMail 组：

`aws workmail create-group --name {{组名}} --organization-id {{组织 ID}}`

- 将成员关联到指定的组：

`aws workmail associate-member-to-group --group-id {{组 ID}} --member-id {{成员 ID}} --organization-id {{组织 ID}}`

- 从 WorkMail 中注销并禁用一个用户或组：

`aws workmail deregister-from-work-mail --entity-id {{实体 ID}} --organization-id {{组织 ID}}`

- 从组织中删除一个用户：

`aws workmail delete-user --user-id {{用户 ID}} --organization-id {{组织 ID}}`
