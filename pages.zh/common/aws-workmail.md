# AWS WorkMail

> 管理 Amazon WorkMail。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/index.html>。

- 列出所有 WorkMail 组织：

`aws workmail list-organizations`

- 列出特定组织的所有用户：

`aws workmail list-users --organization-id {{organization_id}}`

- 在特定组织中创建一个 WorkMail 用户：

`aws workmail create-user --name {{username}} --display-name {{name}} --password {{password}} --organization-id {{organization_id}}`

- 注册并启用一个组/用户使用 WorkMail：

`aws workmail register-to-work-mail --entity-id {{entity_id}} --email {{email}} --organization-id {{organization_id}}`

- 在特定组织中创建一个 WorkMail 组：

`aws workmail create-group --name {{group_name}} --organization-id {{organization_id}}`

- 将成员关联到特定组：

`aws workmail associate-member-to-group --group-id {{group_id}} --member-id {{member_id}} --organization-id {{organization_id}}`

- 从 WorkMail 中注销并禁用用户/组：

`aws workmail deregister-from-work-mail --entity-id {{entity_id}} --organization-id {{organization_id}}`

- 从组织中删除用户：

`aws workmail delete-user --user-id {{user_id}} --organization-id {{organization_id}}`