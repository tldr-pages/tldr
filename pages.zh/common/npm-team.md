# npm team

> 管理 npm 登记表中的组织团队。
> 更多信息：<https://docs.npmjs.com/cli/commands/npm-team>.

- 向组织中的团队添加用户：

`npm team add {{organization:team}} {{username}}`

- 从团队中移除用户：

`npm team rm {{organization:team}} {{username}}`

- 在组织中创建新团队：

`npm team create {{organization:team}}`

- 从组织中删除团队：

`npm team destroy {{organization:team}}`

- 列出组织中的所有团队：

`npm team ls {{organization}}`

- 列出特定团队中的所有用户：

`npm team ls {{organization:team}}`